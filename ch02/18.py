# -*- coding: utf-8 -*-

lines = list(open("./hightemp.txt"))

lines.sort(key = lambda x: -float(x.split()[2]))

print("".join(lines))

