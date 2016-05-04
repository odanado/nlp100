from sec30 import read
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

sentences = read()
words = []

for sentence in sentences:
    for morpheme in sentence:
        words.append(morpheme['base'])

counter = Counter(words)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.hist(list(counter.values()), bins=50)
fig.show()
plt.show()


