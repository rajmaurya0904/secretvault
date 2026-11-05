#!/usr/bin/env python3
"""Bump the patch version in pyproject.toml.

This script reads the project's ``pyproject.toml`` file, increments the
patch component of the version number (``MAJOR.MINOR.PATCH``), writes the
updated file back, and prints the new version string.

The script is intentionally lightweight and does not depend on external
packages. It uses the standard library only.
"""

import re
import sys
from pathlib import Path

PYPROJECT_PATH = Path("pyproject.toml")

VERSION_RE = re.compile(r"^\s*version\s*=\s*['\"](?P<ver>\d+\.\d+\.\d+)['\"]\s*$")


def read_version(path: Path) -> str:
    """Return the current version string from *path*.

    Raises ``RuntimeError`` if the file does not contain a valid version line.
    """
    for line in path.read_text().splitlines():
        m = VERSION_RE.match(line)
        if m:
            return m.group("ver")
    raise RuntimeError("Could not find a valid version line in pyproject.toml")


def bump_patch(version: str) -> str:
    """Return a new version string with the patch component incremented."""
    major, minor, patch = map(int, version.split("."))
    patch += 1
    return f"{major}.{minor}.{patch}"


def write_version(path: Path, new_version: str) -> None:
    """Replace the version line in *path* with *new_version*.

    The function preserves all other content and formatting.
    """
    lines = path.read_text().splitlines()
    new_lines = []
    replaced = False
    for line in lines:
        if VERSION_RE.match(line):
            new_lines.append(f"version = \"{new_version}\"")
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        raise RuntimeError("Could not replace version line in pyproject.toml")
    path.write_text("\n".join(new_lines) + "\n")


def main() -> None:
    if not PYPROJECT_PATH.exists():
        print("pyproject.toml not found", file=sys.stderr)
        sys.exit(1)
    current = read_version(PYPROJECT_PATH)
    new = bump_patch(current)
    write_version(PYPROJECT_PATH, new)
    print(new)


if __name__ == "__main__":
    main()
