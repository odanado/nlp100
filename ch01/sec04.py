# -*- coding: utf-8 -*-

import re

first = [1, 5, 6, 7, 8, 9, 15, 16, 19]
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

arr = re.split('\W+', s)

dist = {}
print(arr)

for i in range(len(arr)):
    if len(arr[i]) > 0:
        if i in first:
            dist[arr[i][0]] = i
        else:
            dist[arr[i][:2]] = i

print(dist)


