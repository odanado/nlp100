from sec30 import read
from collections import Counter
import matplotlib.pyplot as plt

sentences = read()
words = []

for sentence in sentences:
    for morpheme in sentence:
        words.append(morpheme['base'])

counter = Counter(words)
plt.plot(sorted(list(counter.values()), reverse=True), range(1, len(counter)+1), '.')

"""
ordered = counter.most_common()
x = []
y = []
for elem in ordered:
    x.append(elem[1])
    y.append(ordered.index(elem))

plt.plot(x, y, '.')
"""
plt.xscale('log')
plt.yscale('log')
plt.show()
