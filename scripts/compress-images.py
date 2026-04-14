#!/usr/bin/env python3
"""Pre-commit hook: compress images with pngquant / jpegoptim / gifsicle / cwebp.

Works on macOS, Linux, and Windows (tools must be on PATH).
Only replaces the file when compression saves at least 15%.
"""

import os
import shutil
import subprocess
import sys
import tempfile

THRESHOLD = 0.85  # replace only if new_size < 85% of original
MIN_SIZE = 50 * 1024  # skip files smaller than 50 KB

TOOLS = {
    ".png": {
        "check": "pngquant",
        "cmd": lambda src, dst: ["pngquant", "--quality=65-90", "--force", "--output", dst, src],
    },
    ".jpg": {
        "check": "jpegoptim",
        "cmd": lambda src, _dst: ["jpegoptim", "--max=85", "--strip-all", src],
        "in_place": True,
    },
    ".jpeg": {
        "check": "jpegoptim",
        "cmd": lambda src, _dst: ["jpegoptim", "--max=85", "--strip-all", src],
        "in_place": True,
    },
    ".gif": {
        "check": "gifsicle",
        "cmd": lambda src, _dst: ["gifsicle", "-O3", "--batch", src],
        "in_place": True,
    },
    ".webp": {
        "check": "cwebp",
        "cmd": lambda src, dst: ["cwebp", "-q", "85", src, "-o", dst],
    },
}


def compress(filepath: str) -> bool:
    ext = os.path.splitext(filepath)[1].lower()
    tool = TOOLS.get(ext)
    if not tool:
        return False
    if not shutil.which(tool["check"]):
        return False

    orig_size = os.path.getsize(filepath)
    if orig_size < MIN_SIZE:
        return False

    if tool.get("in_place"):
        backup = filepath + ".bak"
        shutil.copy2(filepath, backup)
        try:
            subprocess.run(tool["cmd"](filepath, ""), capture_output=True, timeout=30)
            new_size = os.path.getsize(filepath)
            if new_size >= orig_size * THRESHOLD:
                shutil.move(backup, filepath)
                return False
            os.unlink(backup)
            return True
        except Exception:
            if os.path.exists(backup):
                shutil.move(backup, filepath)
            return False
    else:
        fd, tmp = tempfile.mkstemp(suffix=ext)
        os.close(fd)
        try:
            subprocess.run(tool["cmd"](filepath, tmp), capture_output=True, timeout=30)
            if os.path.exists(tmp) and os.path.getsize(tmp) > 0:
                new_size = os.path.getsize(tmp)
                if new_size < orig_size * THRESHOLD:
                    shutil.move(tmp, filepath)
                    return True
            if os.path.exists(tmp):
                os.unlink(tmp)
            return False
        except Exception:
            if os.path.exists(tmp):
                os.unlink(tmp)
            return False


def main() -> int:
    modified = False
    for filepath in sys.argv[1:]:
        if compress(filepath):
            subprocess.run(["git", "add", filepath], capture_output=True)
            modified = True
    return 1 if modified else 0


if __name__ == "__main__":
    sys.exit(main())
