# -*- coding: utf-8 -*-
def cipher(s):
    return "".join([chr(219 - ord(c)) if c.islower() else c for c in s])

s = "abc()ABC"
print(cipher(s))

