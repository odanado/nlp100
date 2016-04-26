# -*- coding: utf-8 -*-

f = open("./hightemp.txt")

print("".join(set([x.split()[0] + '\n' for x in f])))
