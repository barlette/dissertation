#!/usr/bin/python

import subprocess, sys

commands = [
    ['pdflatex', '-interaction=nonstopmode', sys.argv[1] + '.tex'],
    ['bibtex', sys.argv[1] + '.aux'],
    ['pdflatex', '-interaction=nonstopmode', sys.argv[1] + '.tex'],
    ['pdflatex', '-interaction=nonstopmode', sys.argv[1] + '.tex']
]

for c in commands:
    subprocess.call(c)
