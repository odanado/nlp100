# -*- coding: utf-8 -*-

import sys

lines = list(open("./hightemp.txt"))

n = int(sys.argv[1])
m = int(len(lines) / n)

# http://docs.python.jp/2/library/functions.html?highlight=zip#zip
for (i, x) in enumerate(zip(*[iter(lines)]*m)):
    f = open("%d.out" % i, "w")
    f.write("".join(x))

