"""Validate evidence line ranges before hashing text bytes; no behavior model."""
import hashlib


def checked_range_sha256(data, start, end, hash_bytes=None):
    lines = data.splitlines(keepends=True)
    if (type(start) is not int or type(end) is not int
            or not 1 <= start <= end <= len(lines)):
        raise ValueError(f"Invalid evidence range {start}..{end}; actual lines={len(lines)}")
    chunk = b"".join(lines[start - 1:end])
    if hash_bytes is None:
        return hashlib.sha256(chunk).hexdigest()
    return hash_bytes(chunk)
