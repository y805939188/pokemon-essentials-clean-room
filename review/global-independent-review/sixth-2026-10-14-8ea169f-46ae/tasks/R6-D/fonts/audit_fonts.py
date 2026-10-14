"""Fixed-input, standard-library binary audit. Never imports or runs reference code.

All writes are restricted to this task's directory. No rendering, font registration,
hint bytecode execution, deserialization, downloads, or installation is performed.
"""
from pathlib import Path
import collections
import hashlib
import json
import struct
import subprocess

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-D/fonts'
REF = ROOT / 'reference/pokemon-essentials'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
MAIN_TREE = '6ab3429170d2762607fbc2237014c3a160449fa1'
FORMAL_TREE = '1046fbb657882e84b3dfc6d017943a9edf7782e5'
REF_HEAD = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
FONT_NAMES = ('power clear bold.ttf', 'power clear.ttf', 'power green narrow.ttf',
              'power green small.ttf', 'power green.ttf', 'power red and blue intl.ttf',
              'power red and blue.ttf', 'power red and green.ttf')


def save(name, obj):
    p = OUT / name
    assert p.parent == OUT and OUT.is_dir()
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def log(name, obj):
    with (OUT / name).open('a') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')


def git(cwd, *args):
    cmd = ['git', *args]
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, check=True)
    log('command-log.jsonl', {'command': cmd, 'cwd': str(cwd), 'exit': r.returncode})
    return r.stdout


def fixed_bytes(rel):
    p = REF / rel
    assert p.resolve().is_relative_to(REF.resolve())
    b = p.read_bytes()
    assert b == git(REF, 'show', REF_HEAD + ':' + rel), 'working input differs from fixed commit'
    log('reading-ledger.jsonl', {'path': str(p.relative_to(ROOT)), 'bytes': [0, len(b)],
        'kind': 'structure', 'method': 'independent complete bounded binary parser',
        'sha256': hashlib.sha256(b).hexdigest(), 'fixed_commit': REF_HEAD})
    return b


class R:
    def __init__(self, b):
        self.b = b

    def at(self, fmt, pos):
        size = struct.calcsize('>' + fmt)
        assert 0 <= pos <= len(self.b) - size, (fmt, pos, len(self.b))
        return struct.unpack_from('>' + fmt, self.b, pos)

    def one(self, fmt, pos):
        return self.at(fmt, pos)[0]

    def cut(self, pos, n):
        assert 0 <= pos <= len(self.b) and 0 <= n <= len(self.b) - pos
        return self.b[pos:pos+n]


def checksum(b):
    b += bytes((-len(b)) % 4)
    return sum(struct.unpack('>' + 'I' * (len(b) // 4), b)) & 0xFFFFFFFF


def fields(r, names, fmts, pos=0):
    vals = r.at(fmts, pos)
    assert len(vals) == len(names.split())
    return dict(zip(names.split(), vals))


def cmap_table(b, glyph_count):
    r = R(b)
    version, n = r.at('HH', 0)
    records = []
    subtables = {}
    for i in range(n):
        platform, encoding, off = r.at('HHI', 4 + 8*i)
        records.append({'platform': platform, 'encoding': encoding, 'offset': off})
        if off in subtables:
            continue
        fmt, length, language = r.at('HHH', off)
        s = R(r.cut(off, length))
        item = {'format': fmt, 'length': length, 'language': language}
        mappings = []
        if fmt == 0:
            assert length == 262
            mappings = list(enumerate(s.cut(6, 256)))
        elif fmt == 4:
            seg2, sr, es, rs = s.at('HHHH', 6)
            assert seg2 % 2 == 0
            nseg = seg2 // 2
            ends = s.at('H'*nseg, 14)
            assert s.one('H', 14 + seg2) == 0
            starts = s.at('H'*nseg, 16 + seg2)
            deltas = s.at('h'*nseg, 16 + seg2*2)
            ranges = s.at('H'*nseg, 16 + seg2*3)
            item['search_fields'] = [sr, es, rs]
            item['segments'] = []
            for j, (a, z, delta, ro) in enumerate(zip(starts, ends, deltas, ranges)):
                assert a <= z and (j == 0 or a > ends[j-1])
                item['segments'].append([a, z, delta, ro])
                for cp in range(a, z+1):
                    if ro:
                        gid = s.one('H', 16 + seg2*3 + 2*j + ro + 2*(cp-a))
                        gid = (gid + delta) & 0xFFFF if gid else 0
                    else:
                        gid = (cp + delta) & 0xFFFF
                    mappings.append((cp, gid))
            assert ends[-1] == 0xFFFF
        else:
            raise AssertionError(('unexpected cmap format', fmt))
        assert all(gid < glyph_count for _, gid in mappings)
        item['mappings'] = mappings
        item['nonzero_count'] = sum(gid != 0 for _, gid in mappings)
        subtables[off] = item
    return {'version': version, 'records': records, 'subtables': subtables}


def glyf_table(b, offsets, n):
    glyphs = []
    for gid in range(n):
        start, end = offsets[gid:gid+2]
        assert 0 <= start <= end <= len(b)
        g = {'glyph': gid, 'relative_bytes': [start, end], 'length': end-start}
        glyphs.append(g)
        if start == end:
            g['kind'] = 'empty'
            continue
        r = R(b[start:end])
        contours, xmin, ymin, xmax, ymax = r.at('hhhhh', 0)
        g['stored_bbox'] = [xmin, ymin, xmax, ymax]
        g['contours'] = contours
        pos = 10
        if contours >= 0:
            g['kind'] = 'simple'
            ends = r.at('H'*contours, pos) if contours else ()
            assert all(a < z for a, z in zip(ends, ends[1:]))
            pos += 2*contours
            instructions = r.one('H', pos)
            pos += 2
            g['instruction_length'] = instructions
            g['instruction_sha256'] = hashlib.sha256(r.cut(pos, instructions)).hexdigest()
            pos += instructions
            count = ends[-1] + 1 if contours else 0
            flags = []
            while len(flags) < count:
                flag = r.one('B', pos)
                pos += 1
                repeat = r.one('B', pos) if flag & 8 else 0
                pos += bool(flag & 8)
                flags.extend([flag]*(repeat+1))
                assert len(flags) <= count
            axes = []
            for shortbit, samebit in ((2, 16), (4, 32)):
                coord = 0
                axis = []
                for flag in flags:
                    if flag & shortbit:
                        d = r.one('B', pos)
                        pos += 1
                        d = d if flag & samebit else -d
                    elif flag & samebit:
                        d = 0
                    else:
                        d = r.one('h', pos)
                        pos += 2
                    coord += d
                    axis.append(coord)
                axes.append(axis)
            points = [[x, y, bool(flag & 1)] for x, y, flag in zip(*axes, flags)]
            g['contour_end_points'] = ends
            g['points'] = points
            if points:
                actual = [min(axes[0]), min(axes[1]), max(axes[0]), max(axes[1])]
                g['decoded_point_bbox'] = actual
                g['points_within_stored_bbox'] = xmin <= actual[0] <= actual[2] <= xmax and ymin <= actual[1] <= actual[3] <= ymax
        else:
            assert contours == -1
            g['kind'] = 'composite'
            components = []
            while True:
                flag, target = r.at('HH', pos)
                pos += 4
                assert target < n
                word = bool(flag & 1)
                xy = bool(flag & 2)
                fmt = ('h' if xy else 'H') if word else ('b' if xy else 'B')
                args = r.at(fmt*2, pos)
                pos += 4 if word else 2
                matrix = [16384, 0, 0, 16384]
                if flag & 8:
                    v = r.one('h', pos)
                    pos += 2
                    matrix = [v, 0, 0, v]
                elif flag & 64:
                    x, y = r.at('hh', pos)
                    pos += 4
                    matrix = [x, 0, 0, y]
                elif flag & 128:
                    matrix = list(r.at('hhhh', pos))
                    pos += 8
                components.append({'flags': flag, 'glyph': target, 'args_are_xy': xy,
                                   'args': args, 'matrix_f2dot14': matrix})
                if not flag & 32:
                    break
            g['components'] = components
            if flag & 256:
                instructions = r.one('H', pos)
                pos += 2
                g['instruction_length'] = instructions
                g['instruction_sha256'] = hashlib.sha256(r.cut(pos, instructions)).hexdigest()
                pos += instructions
        g['decoded_bytes'] = pos
        padding = r.cut(pos, len(r.b)-pos)
        g['trailing_bytes_hex'] = padding.hex()
    return glyphs


def font_audit(name):
    b = fixed_bytes('Fonts/' + name)
    r = R(b)
    scaler, ntables, search, selector, shift = r.at('IHHHH', 0)
    assert scaler == 0x00010000
    tables = []
    data = {}
    for i in range(ntables):
        tag, expected, offset, length = r.at('4sIII', 12+16*i)
        tag = tag.decode('ascii')
        chunk = r.cut(offset, length)
        raw = chunk
        if tag == 'head':
            raw = chunk[:8] + bytes(4) + chunk[12:]
        tables.append({'tag': tag, 'offset': offset, 'length': length,
                       'checksum': f'{expected:08x}', 'calculated_checksum': f'{checksum(raw):08x}',
                       'checksum_matches': checksum(raw) == expected,
                       'sha256': hashlib.sha256(chunk).hexdigest()})
        assert tag not in data
        data[tag] = R(chunk)
    ordered = sorted(tables, key=lambda x: x['offset'])
    assert all(a['offset'] + a['length'] <= z['offset'] for a, z in zip(ordered, ordered[1:]))
    gaps = []
    cursor = 12 + 16*ntables
    for t in ordered:
        assert cursor <= t['offset']
        gaps.append({'bytes': [cursor, t['offset']], 'hex': b[cursor:t['offset']].hex()})
        cursor = t['offset'] + t['length']
    gaps.append({'bytes': [cursor, len(b)], 'hex': b[cursor:].hex()})
    head = fields(data['head'], 'version revision checksumAdjustment magic flags unitsPerEm created modified xMin yMin xMax yMax macStyle lowestRecPPEM fontDirectionHint indexToLocFormat glyphDataFormat', 'IIIIHHQQhhhhHHhhh')
    hhea = fields(data['hhea'], 'version ascender descender lineGap advanceWidthMax minLSB minRSB xMaxExtent caretSlopeRise caretSlopeRun caretOffset reserved1 reserved2 reserved3 reserved4 metricDataFormat numberOfHMetrics', 'IhhhHhhhhhhhhhhhH')
    maxp = fields(data['maxp'], 'version numGlyphs maxPoints maxContours maxCompositePoints maxCompositeContours maxZones maxTwilightPoints maxStorage maxFunctionDefs maxInstructionDefs maxStackElements maxSizeOfInstructions maxComponentElements maxComponentDepth', 'I'+'H'*14)
    n = maxp['numGlyphs']
    nm = hhea['numberOfHMetrics']
    assert 1 <= nm <= n
    assert len(data['hmtx'].b) == nm*4+(n-nm)*2
    metrics = []
    for gid in range(n):
        advance = data['hmtx'].one('H', min(gid, nm-1)*4)
        lsb = data['hmtx'].one('h', gid*4+2) if gid < nm else data['hmtx'].one('h', nm*4+(gid-nm)*2)
        metrics.append({'glyph': gid, 'advance': advance, 'left_side_bearing': lsb})
    assert head['indexToLocFormat'] in (0, 1)
    width = 2 if head['indexToLocFormat'] == 0 else 4
    assert len(data['loca'].b) == (n+1)*width
    offsets = list(data['loca'].at(('H' if width == 2 else 'I')*(n+1), 0))
    if width == 2:
        offsets = [x*2 for x in offsets]
    glyphs = glyf_table(data['glyf'].b, offsets, n)
    cm = cmap_table(data['cmap'].b, n)
    namer = data['name']
    nameformat, count, storage = namer.at('HHH', 0)
    names = []
    for i in range(count):
        platform, enc, lang, nid, length, off = namer.at('HHHHHH', 6+12*i)
        text = namer.cut(storage+off, length)
        codec = 'utf-16-be' if platform in (0, 3) else 'mac_roman' if platform == 1 and enc == 0 else None
        entry = {'platform': platform, 'encoding': enc, 'language': lang, 'name_id': nid,
                 'length': length, 'offset': off, 'sha256': hashlib.sha256(text).hexdigest()}
        if codec and nid in (1, 2, 4, 6):
            entry['value'] = text.decode(codec, errors='strict')
        elif codec:
            entry['decoded_character_count'] = len(text.decode(codec, errors='strict'))
        names.append(entry)
    post = fields(data['post'], 'version italicAngle underlinePosition underlineThickness isFixedPitch minMemType42 maxMemType42 minMemType1 maxMemType1', 'IihhIIIII')
    if post['version'] == 0x20000:
        pn = data['post'].one('H', 32)
        assert pn == n
        indices = list(data['post'].at('H'*n, 34))
        pos = 34+2*n
        custom = []
        while pos < len(data['post'].b):
            length = data['post'].one('B', pos)
            pos += 1
            custom.append(data['post'].cut(pos, length).decode('ascii'))
            pos += length
        assert all(x < 258+len(custom) for x in indices)
        post.update({'glyph_name_indices': indices, 'custom_names': custom,
                     'standard_name_indices': '0..257 retain standard glyph-name index, not Unicode identity'})
    else:
        assert post['version'] == 0x30000 and len(data['post'].b) == 32
    osr = data['OS/2']
    os2 = fields(osr, 'version xAvgCharWidth usWeightClass usWidthClass fsType ySubscriptXSize ySubscriptYSize ySubscriptXOffset ySubscriptYOffset ySuperscriptXSize ySuperscriptYSize ySuperscriptXOffset ySuperscriptYOffset yStrikeoutSize yStrikeoutPosition sFamilyClass', 'HhHHH'+'h'*11)
    os2['panose'] = list(osr.cut(32, 10))
    os2['unicode_ranges'] = list(osr.at('IIII', 42))
    os2['vendor_id'] = osr.cut(58, 4).decode('ascii')
    os2.update(fields(osr, 'fsSelection firstChar lastChar typoAscender typoDescender typoLineGap winAscent winDescent codePageRange1 codePageRange2', 'HHHhhhHHII', 62))
    if os2['version'] >= 2:
        os2.update(fields(osr, 'sxHeight sCapHeight defaultChar breakChar maxContext', 'hhHHH', 86))
    gasp = data['gasp']
    gv, gn = gasp.at('HH', 0)
    gasp_out = {'version': gv, 'ranges': [gasp.at('HH', 4+4*i) for i in range(gn)]}
    assert len(gasp.b) == 4+4*gn
    fftm = fields(data['FFTM'], 'version timestamp created modified', 'IQQQ')
    gd = data['GDEF']
    gdver, classoff, attachoff, ligoff, markoff = gd.at('IHHHH', 0)
    gdef = {'version': gdver, 'glyphClassDef': classoff, 'attachList': attachoff,
            'ligCaretList': ligoff, 'markAttachClassDef': markoff}
    assert attachoff == 0
    classformat = gd.one('H', classoff)
    assert classformat == 2
    classcount = gd.one('H', classoff+2)
    gdef['ranges'] = [gd.at('HHH', classoff+4+6*i) for i in range(classcount)]
    assert all(a <= z < n for a, z, _ in gdef['ranges'])
    gdef['glyph_class_end'] = classoff+4+6*classcount
    coverageoff, ligcount = gd.at('HH', ligoff)
    assert ligcount == 0
    coverage_format, coverage_count = gd.at('HH', ligoff+coverageoff)
    assert coverage_format == 2 and coverage_count == 0
    gdef['ligature_carets'] = {'offset': ligoff, 'ligature_count': ligcount,
        'coverage_relative_offset': coverageoff, 'coverage_format': coverage_format,
        'coverage_range_count': coverage_count}
    markformat, markstart, markcount = gd.at('HHH', markoff)
    assert markformat == 1
    markclasses = gd.at('H'*markcount, markoff+6)
    gdef['mark_attach_classes'] = {'format': markformat, 'start_glyph': markstart,
                                  'classes': markclasses}
    assert len(gd.b) == markoff+6+2*markcount
    unicode_map = dict(next(s['mappings'] for s in cm['subtables'].values() if s['format'] == 4))
    mac_map = dict(next(s['mappings'] for s in cm['subtables'].values() if s['format'] == 0))
    mac_links = []
    for code, gid in mac_map.items():
        cp = ord(bytes([code]).decode('mac_roman'))
        mac_links.append({'mac_code': code, 'unicode_via_mac_roman': cp, 'mac_glyph': gid,
                          'unicode_glyph': unicode_map.get(cp, 0),
                          'same_glyph': gid == unicode_map.get(cp, 0)})
    inverse = collections.defaultdict(list)
    for cp, gid in unicode_map.items():
        inverse[gid].append(cp)
    for g, metric in zip(glyphs, metrics):
        g['unicode_codepoints'] = inverse.get(g['glyph'], [])
        g['metric'] = metric
    summary = {'name': name, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
        'tables': ntables, 'glyphs': n, 'units_per_em': head['unitsPerEm'],
        'unicode_nonzero': sum(gid != 0 for gid in unicode_map.values()),
        'unicode_has_CJK_4E00': unicode_map.get(0x4E00, 0) != 0,
        'kinds': dict(collections.Counter(g['kind'] for g in glyphs)),
        'bad_table_checksums': [t['tag'] for t in tables if not t['checksum_matches']],
        'sfnt_checksum': f'{checksum(b):08x}',
        'nonzero_padding': sum(bool(bytes.fromhex(g['hex']).strip(bytes(1))) for g in gaps),
        'bad_simple_bboxes': [g['glyph'] for g in glyphs if g.get('points_within_stored_bbox') is False],
        'mac_unicode_same_glyph': sum(x['same_glyph'] for x in mac_links),
        'probe_glyphs': {f'U+{cp:04X}': unicode_map.get(cp, 0) for cp in (32,65,66,0xE9,0x2640,0x2642,0x4E00)}}
    return {'summary': summary, 'sfnt': {'scaler': scaler, 'searchRange': search,
        'entrySelector': selector, 'rangeShift': shift}, 'tables': tables,
        'all_nontable_byte_gaps': gaps, 'head': head, 'hhea': hhea, 'maxp': maxp,
        'OS2': os2, 'hmtx': metrics, 'loca': offsets, 'cmap': cm,
        'glyphs': glyphs, 'name': {'format': nameformat, 'records': names},
        'post': post, 'GDEF': gdef, 'gasp': gasp_out, 'FFTM': fftm,
        'mac_roman_unicode_glyph_links': mac_links}


def bmp_audit(name):
    b = fixed_bytes(name)
    assert b[:2] == b'BM'
    file_size, res1, res2, pixel_offset = struct.unpack_from('<IHHI', b, 2)
    header_size, width, height, planes, depth, compression, image_size, xppm, yppm, used, important = struct.unpack_from('<IiiHHIIiiII', b, 14)
    assert (file_size, header_size, width, height, planes, depth, compression) == (246,40,8,8,1,24,0)
    assert file_size == len(b)
    stride = ((width*depth+31)//32)*4
    assert pixel_offset + stride*abs(height) == len(b)
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            pos = pixel_offset+(height-1-y)*stride+x*3
            blue, green, red = b[pos:pos+3]
            row.append([red,green,blue])
        pixels.append(row)
    histogram = collections.Counter(tuple(rgb) for row in pixels for rgb in row)
    return {'path': name, 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b),
        'header': {'file_size': file_size, 'reserved': [res1,res2], 'pixel_offset': pixel_offset,
        'DIB_size': header_size, 'width': width, 'height': height, 'planes': planes,
        'depth': depth, 'compression': compression, 'image_size': image_size,
        'x_pixels_per_metre': xppm, 'y_pixels_per_metre': yppm,
        'colors_used': used, 'important_colors': important},
        'byte_ranges': {'file_header': [0,14], 'DIB': [14,54],
        'pre_pixel_gap': [54,pixel_offset], 'pixels_and_padding': [pixel_offset,len(b)]},
        'row_stride': stride, 'row_padding_bytes': stride-width*3,
        'pixels_RGB_top_to_bottom_left_to_right': pixels,
        'histogram': [{'RGB': list(k), 'count': v} for k,v in sorted(histogram.items())],
        'alpha_channel': False, 'browser_rendering': 'UNKNOWN_NOT_EXECUTED'}


def main():
    assert git(ROOT, 'rev-parse', 'HEAD', 'HEAD^{tree}', 'HEAD:deliverables/final-specification-set').decode().splitlines() == [MAIN, MAIN_TREE, FORMAL_TREE]
    assert git(REF, 'rev-parse', 'HEAD', 'HEAD^{tree}').decode().splitlines() == [REF_HEAD, REF_TREE]
    fonts = [font_audit(name) for name in FONT_NAMES]
    for name, result in zip(FONT_NAMES, fonts):
        save(name.replace('.ttf', '').replace(' ', '-')+'.json', result)
    bmps = [bmp_audit(name) for name in ('knownpoint.bmp', 'selpoint.bmp')]
    save('bmp-full-pixels.json', bmps)
    save('binary-summary.json', {'fonts': [f['summary'] for f in fonts], 'BMPs': [
        {'path': x['path'], 'histogram': x['histogram']} for x in bmps],
        'limits': ['No host font discovery/registration or rasterization',
        'No shaping, hint execution, native measurement, browser execution or GPU testing',
        'No composite glyphs occur in the fixed inputs; generic composite support is not certified',
        'Byte parse is structural evidence, not complete font/UI behavioral coverage']})
    log('command-log.jsonl', {'command': ['python3', str(OUT/'audit_fonts.py')],
        'exit': 0, 'source_reviewed_before_execution': True,
        'reference_program_execution': False, 'purpose': 'fixed-input structural binary audit'})
    print(json.dumps({'fonts': [f['summary'] for f in fonts], 'BMPs': bmps}, ensure_ascii=False))


if __name__ == '__main__':
    main()
