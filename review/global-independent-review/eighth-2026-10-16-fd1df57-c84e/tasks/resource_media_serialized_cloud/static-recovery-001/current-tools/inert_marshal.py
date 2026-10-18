"""Data-only Ruby Marshal 4.8 reader for the two fixed R artifacts.

Only nil/bool/fixnum/float/bignum/symbol/string/array/hash/ivar/link tags are
accepted. Class objects, user-defined marshaling and executable loading fail
closed. Links remain explicit, and no reference object is instantiated.
"""
from pathlib import Path
import collections, hashlib, json, struct, subprocess, zlib

ROOT=Path(__file__).resolve().parents[1]
REF=Path('/workspace/pokemon-essentials')
class Parser:
    def __init__(self,data):
        self.data=data; self.pos=0; self.symbols=[];self.objects=[];self.nodes=[];self.counts=collections.Counter()
    def take(self,n):
        if n<0 or self.pos+n>len(self.data):raise ValueError('out of bounds')
        start=self.pos;self.pos+=n;return self.data[start:self.pos]
    def integer(self):
        c=int.from_bytes(self.take(1),'little',signed=True)
        if c==0:return 0
        if c>4:return c-5
        if c< -4:return c+5
        raw=int.from_bytes(self.take(abs(c)),'little')
        return raw if c>0 else raw-(1<<(8*abs(c)))
    def value(self,depth=0):
        if depth>128:raise ValueError('depth')
        start=self.pos; tag=self.take(1).decode('ascii');self.counts[tag]+=1
        n={'type':tag,'start':start};self.nodes.append(n)
        if tag=='0':n['value']=None
        elif tag in ['T','F']:n['value']=tag=='T'
        elif tag=='i':n['value']=self.integer()
        elif tag==':':
            n['value']=self.take(self.integer()).decode('utf8');n['symbol_index']=len(self.symbols);self.symbols.append(n['value'])
        elif tag==';':
            i=self.integer();n['symbol_index']=i;n['value']=self.symbols[i]
        elif tag=='@':
            i=self.integer()
            if not 0<=i<len(self.objects):raise ValueError('object link')
            n['object_index']=i
        elif tag=='I':
            n['wrapped']=self.value(depth+1);n['ivars']=[[self.value(depth+1),self.value(depth+1)] for _ in range(self.integer())]
        elif tag in ['"','[','{','}','f','l']:
            n['object_index']=len(self.objects);self.objects.append(n)
            if tag=='"':
                raw=self.take(self.integer());n['bytes_hex']=raw.hex();n['byte_length']=len(raw)
                try:n['text_utf8']=raw.decode('utf8')
                except UnicodeDecodeError:n['text_utf8']=None
            elif tag=='[':n['items']=[self.value(depth+1) for _ in range(self.integer())]
            elif tag in ['{','}']:
                n['pairs']=[[self.value(depth+1),self.value(depth+1)] for _ in range(self.integer())]
                if tag=='}':n['default']=self.value(depth+1)
            elif tag=='f':n['literal']=self.take(self.integer()).decode('ascii')
            else:
                sign=self.take(1);size=self.integer();magnitude=int.from_bytes(self.take(size*2),'little');n['value']=magnitude*(-1 if sign==b'-' else 1)
        else:raise ValueError('unsupported data tag '+repr(tag))
        n['end_exclusive']=self.pos;return n
    def read(self):
        if self.take(2)!=b'\x04\x08':raise ValueError('version')
        result=self.value()
        if self.pos!=len(self.data):raise ValueError('trailing bytes')
        return result
def univar(n):
    while n['type']=='I':n=n['wrapped']
    return n
def main():
    summaries=[]
    for name in ['Data/Scripts.rxdata','Data/messages_core.dat']:
        data=(REF/name).read_bytes()
        frozen=subprocess.run(['git','-C',str(REF),'show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+name],check=True,capture_output=True).stdout
        assert data==frozen, 'frozen R bytes changed: '+name
        p=Parser(data);result=p.read()
        artifact={'source':{'path':name,'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()},'root':result,'summary':{'parsed_bytes':p.pos,'node_counts':dict(p.counts),'objects':len(p.objects),'symbols':len(p.symbols),'status':'STRUCTURE_PARSED_COMPLETE','object_or_source_execution':False}}
        dest=ROOT/'current-serialized';dest.mkdir(exist_ok=True)
        (dest/(Path(name).name+'.json')).write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n')
        summaries.append({'path':name,**artifact['summary']})
        if name=='Data/Scripts.rxdata':
            items=result['items'];assert len(items)==1
            record=items[0]['items'];assert record[0]['value']==62054200
            title=univar(record[1]);assert title['text_utf8']=='Main'
            payload=univar(record[2]);compressed=bytes.fromhex(payload['bytes_hex'])
            decoder=zlib.decompressobj();plain=decoder.decompress(compressed,1000000)
            assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
            (dest/'Main.rb').write_bytes(plain)
            (dest/'Main.identity.json').write_text(json.dumps({'serialized_string_node_range':[payload['start'],payload['end_exclusive']],'compressed_payload_range':[payload['end_exclusive']-len(compressed),payload['end_exclusive']],'compressed_bytes':len(compressed),'compressed_sha256':hashlib.sha256(compressed).hexdigest(),'decoded_bytes':len(plain),'decoded_lines':len(plain.splitlines()),'decoded_sha256':hashlib.sha256(plain).hexdigest(),'status':'DECODED_NOT_EXECUTED'},indent=2)+'\n')
    (ROOT/'current-serialized/summary.json').write_text(json.dumps(summaries,indent=2)+'\n')
    print(json.dumps(summaries))
if __name__=='__main__':main()
