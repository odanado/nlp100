from sec30 import read
from collections import Counter
import matplotlib.pyplot as plt

sentences = read()

words = []

for sentence in sentences:
    for morpheme in sentence:
        words.append(morpheme['base'])

counter = Counter(words)
x = []
y = []
for word, cnt in counter.most_common(10):
    y.append(cnt)
    x.append(len(y))

print(words[:10])
plt.bar(x, y, align='center')
plt.xticks(x, words[:10])
plt.show()
