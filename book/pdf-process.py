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
            line = f.readline().replace(r'\subsection{', r'\subsection*{').replace(r'\begin{verbatim}', r'\begin{lstlisting}').replace(r'\end{verbatim}', r'\end{lstlisting}')
            if line.startswith(r'\subsection*{Tags}'):
                TAGS=True
                continue
            if TAGS and len(line.strip()) > 0:
                print '\n'.join(map(lambda x: r'\index{%s}' % x, map(str.strip, line.split(','))))
                TAGS=False
                continue
            if line == r'\\documentclass[]{article}':
                continue
            if line.startswith(r'\section{Title}'):
                TITLE=True
                continue
            if TITLE and len(line.strip()) > 0:
                print r'\section{%s}' % line.strip()
                TITLE=False
                continue
            if line.startswith(r'\subsection*{Difficulty}'):
                DIFFICULTY=True
                continue
            if DIFFICULTY:
                if line.startswith(r'\subsection*{'):
                    DIFFICULTY=False
                    print line,
                    continue
                else:
                    continue
            if line.startswith(r'\subsection*{'):
                if 'Solution}' in line:
                    CODE=True
                    print line,
                    try: LANG=re.findall(r"section..([A-Za-z]+) [Ss]olution}", line, re.I)[0]
                    except IndexError:
                        LANG="javascript"
                    continue
            if CODE and line.startswith(r'\begin{lstlisting}'):
                print r'''\begin{mdframed}[linecolor=black, topline=true, bottomline=true, leftline=false, rightline=false, backgroundcolor=white, userdefinedwidth=\textwidth]'''
                print r'\begin{minted}'
                print MINTEDOPS,
                print '{%s}' % MINTLANGMAPS.get(LANG, LANG.lower())
                LANG=None
                continue
            if CODE and line.startswith(r'\end{lstlisting}'):
                print r'\end{minted}'
                print r'\end{mdframed}'
                CODE=False
                continue
            print line,

if __name__ == '__main__':
    main()
