# -*- coding: utf-8 -*-

def n_gram(sentence, n):
    return [sentence[i:i+n] for i in range(len(sentence))]

s1 = "paraparaparadise"
s2 = "paragraph"
set1 = set(n_gram(s1, 2))
set2 = set(n_gram(s2, 2))

print(set1)
print(set2)
print(set1.union(set2))
print(set1.difference(set2))
print(set1.intersection(set2))
print("se" in set1.intersection(set2))

