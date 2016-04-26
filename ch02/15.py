# -*- coding: utf-8 -*-

import sys

lines = list(open("./hightemp.txt"))

n = int(sys.argv[1])

print("".join(lines[-n:]))

