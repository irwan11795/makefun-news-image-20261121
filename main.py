#!/usr/bin/env python3
"""Entry point for news-image-20261121.

Copies the pre-rendered entry.png (built locally by gen.py) into the
output directory and verifies its SHA-256 before finishing, so a
corrupt or stale image can never be submitted silently.

Standard library only: the grading sandbox has no Pillow, so this
file must not import anything beyond the stdlib.
"""
import hashlib
import os
import shutil
import sys
import tempfile

EXPECTED_SHA256 = (
    "37a403e792c8895e593de9513a1457638fafc5b014a340d992da3100dcdc577b"
)
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def resolve_output_dir():
    """MAKEFUN_OUTPUT_DIR -> /output -> output/ -> tmpdir."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    if os.path.isdir("output"):
        return "output"
    return tempfile.mkdtemp(prefix="makefun-output-")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: pre-rendered image not found: {SOURCE}",
              file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(dest, "rb") as fh:
        magic = fh.read(8)
    if magic != PNG_MAGIC:
        print(f"error: {dest} is not a PNG file", file=sys.stderr)
        os.remove(dest)
        return 1
    size = os.path.getsize(dest)
    if size > MAX_BYTES:
        print(f"error: {dest} is {size} bytes, over the "
              f"{MAX_BYTES} byte limit", file=sys.stderr)
        os.remove(dest)
        return 1
    actual = sha256_file(dest)
    if actual != EXPECTED_SHA256:
        print(f"error: sha256 mismatch for {dest}\n"
              f"  expected: {EXPECTED_SHA256}\n"
              f"  actual:   {actual}", file=sys.stderr)
        os.remove(dest)
        return 1
    print(f"wrote {dest} ({size} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
