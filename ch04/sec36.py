from sec30 import read
from collections import Counter

sentences = read()

# collections.Counterについて
# http://qiita.com/hatchinee/items/a904c1f8d732a4686c9d

words = []

for sentence in sentences:
    for morpheme in sentence:
        words.append(morpheme['base'])

counter = Counter(words)
for word, cnt in counter.most_common():
    print(word, cnt)

"""

counter = {}

for sentence in sentences:
    for morpheme in sentence:
        word = morpheme['base']
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

print(sorted(counter.items(), key=lambda x:-x[1]))

"""
