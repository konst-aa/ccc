#! /usr/bin/env nix-shell
#! nix-shell --pure -i python -p python3 python3Packages.docopt


__doc__ = """purge, call in the directory you want to purge.

Usage:
    purge.py [--ignore=<dirs>...]
    invert.py (-h | --help)
    invert.py (--version)

Options:
    [--ignore=<dirs>...] Directories to ignore.
    (-h | --help) Show this screen.
    (--version) Show version.

"""

from docopt import docopt
import os

EXTENSIONS = [".out", ".in"]

def getextension(file):
    parts = os.path.splitext(file)
    return parts[-1]

if __name__ == "__main__":
    arguments = docopt(__doc__, version="invert v1")
    out = arguments["<out>"]
    abs_here = os.path.abspath(".")

    ignore_check = lambda path: path not in arguments["--ignore"] + ["invert.py"] + [
        out
    ]

    for root, dirs, files in os.walk("."):
        files = [f for f in files if ignore_check(f)]
        dirs[:] = [d for d in dirs if ignore_check(d)]
        for file in files:
            t = getextension(file)
            if t in EXTENSIONS:
                os.remove(f"{root}/{file}")
