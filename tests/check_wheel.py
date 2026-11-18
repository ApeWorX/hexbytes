"""Check the installable files in a built hexbytes wheel."""

import sys
from zipfile import ZipFile


def check_wheel(path: str) -> None:
    with ZipFile(path) as wheel:
        files = {name for name in wheel.namelist() if not name.endswith("/")}
    unexpected = sorted(
        name
        for name in files
        if not name.startswith("hexbytes/")
        and not name.split("/", 1)[0].endswith(".dist-info")
    )
    if unexpected:
        raise ValueError(f"Unexpected wheel files: {unexpected}")
    missing = {"hexbytes/__init__.py", "hexbytes/py.typed"} - files
    if missing:
        raise ValueError(f"Missing package files: {sorted(missing)}")


if __name__ == "__main__":
    check_wheel(sys.argv[1])
