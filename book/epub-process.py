#!/usr/bin/env python

import re
import sys

MINTEDOPS = r"""    [
    framesep=2mm,
    baselinestretch=1.2,
    fontsize=\footnotesize,
    breaklines,
    linenos
    ]
"""

MINTLANGMAPS={r'F\#': 'ocaml',
              'Fsharp': 'ocaml',
              'Scala': 'javascript',
              'Go': 'go'}

def main():
    TITLE=False
    DIFFICULTY=False
    CODE=False
    LANG=None
    TAGS=False
    line=True
    with sys.stdin as f:
        while line:
            line = f.readline()
            # skip tags
            if line.startswith("## Tags"):
                TAGS=True
                continue
            if TAGS and len(line.strip()) > 0:
                TAGS=False
                continue
            if line.startswith("# Title"):
                TITLE=True
                print
                continue
            if TITLE and len(line.strip()) > 0:
                print '# %s' % line.strip()
                TITLE=False
                continue
            if line.startswith("## Difficulty"):
                DIFFICULTY=True
                continue
            if line.strip() == "## Description": 
                continue
            if DIFFICULTY and len(line.strip()) > 0:
                DIFFICULTY=False
                continue
            print line,

if __name__ == '__main__':
    main()
