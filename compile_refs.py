#!/usr/bin/python

import subprocess, sys

#print(sys.argv[1])
#print(sys.argv[2])

if sys.argv[1] == '-d':
	#print('aaa')
	commands = [
    		['pdflatex', '-interaction=nonstopmode', sys.argv[2]],
    		['bibtex', sys.argv[2]],
    		['pdflatex', '-interaction=nonstopmode', sys.argv[2]],
    		['pdflatex', '-interaction=nonstopmode', sys.argv[2]],
    		['cp', sys.argv[2] + '.pdf', '/mnt/d/Dropbox/dissertation/']
	]
else:
	commands = [
    		['pdflatex', sys.argv[1] + '.tex'],
    		['bibtex', sys.argv[1] + '.aux'],
    		['pdflatex', sys.argv[1] + '.tex'],
    		['pdflatex', sys.argv[1] + '.tex'],
    		['cp', sys.argv[1] + '.pdf', '/mnt/d/Dropbox/dissertation/']
	]

for c in commands:
	print(c)
	subprocess.call(c)
