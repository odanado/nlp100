# -*- coding: utf-8 -*-

col1 = open("./col1.txt")
col2 = open("./col2.txt")

for (line1, line2) in zip(col1, col2):
    print("%s\t%s" % (line1.rstrip(), line2.rstrip()))

