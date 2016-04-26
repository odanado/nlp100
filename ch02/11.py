# -*- coding: utf-8 -*-

f = open("./hightemp.txt")

for line in f:
    print line.replace('\t', ' '),

