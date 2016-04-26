# -*- coding: utf-8 -*-

lines = list(open("./hightemp.txt"))
prefectures = [x.split()[0] for x in lines]

lines.sort(key = lambda x: (-prefectures.count(x.split()[0]), x.split()[0]))

print("".join(lines))

