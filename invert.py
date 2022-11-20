#! /usr/bin/env nix-shell
#! nix-shell --pure -i python -p python3 pythonPackages.docopt


__doc__ = """invert, call in the directory you wish to invert.

Usage:
    invert.py <out> [--ignore=<dirs>...]
    invert.py (-h | --help)
    invert.py (--version)

Options:
    [--ignore=<dirs>...] Directories to ignore.
    (-h | --help) Show this screen.
    (--version) Show version.

"""

from docopt import docopt
import os

LANGS = {
    ".py":"python",
    ".hs":"haskell",
    ".exs":"elixir",
    ".scm":"scheme",
    ".rkt":"scheme"
}

def getextension(file):
    parts = os.path.splitext(file)
    return parts[-1]

if __name__ == '__main__':
    arguments = docopt(__doc__, version='invert v1')
    out = arguments["<out>"]
    abs_here = os.path.abspath(".")

    hidden_check = lambda path: not path.startswith(".")
    ignore_check = lambda path: path not in arguments["--ignore"] + ["invert.py"] + [out]

    langs = {}
    for root, dirs, files in os.walk("."):
        files = [f for f in files if hidden_check(f) and ignore_check(f)]
        dirs[:] = [d for d in dirs if hidden_check(d) and ignore_check(d)]
        for file in files:
            t = getextension(file)
            if t in LANGS:
                lang = LANGS[t]
                langs[lang] = {} if lang not in langs else langs[lang]
                langs[lang][root] = [] if root not in langs[lang] else langs[lang][root]
                langs[lang][root] += [file]

    for lang, subdirs in langs.items():
        for subdir, files in subdirs.items():
            for file in files:
                target_dir = f"{abs_here}/{out}/{lang}/{subdir}"
                os.makedirs(target_dir, exist_ok=True)
                try:
                    os.symlink(f"{abs_here}/{subdir}/{file}", f"{target_dir}/{file}")
                except FileExistsError:
                    pass
