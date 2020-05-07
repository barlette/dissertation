#!/usr/bin/python

import subprocess, sys

commands = [
    ['pdflatex', sys.argv[1] + '.tex'],
    ['bibtex', sys.argv[1] + '.aux'],
    ['pdflatex', sys.argv[1] + '.tex'],
    ['pdflatex', sys.argv[1] + '.tex'],
    ['mv', sys.argv[1] + '.pdf', '/mnt/d/Dropbox/dissertation/']
]

for c in commands:
    subprocess.call(c)
