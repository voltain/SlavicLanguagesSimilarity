#!/usr/bin/env python
mainlist = []
infile = open('basic_words2.txt','r')
for line in infile:
    mainlist.append(line.strip().split(','))

infile.close()

print mainlist