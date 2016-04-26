# -*- coding: utf-8 -*-
import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
a = s.split()
b = a[1:-1]
random.shuffle(b)
a[1:-1] = b
print(" ".join(a))
