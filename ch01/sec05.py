# -*- coding: utf-8 -*-
def n_gram(sentence, n):
    return [sentence[i:i+n] for i in range(len(sentence))]

sentence = "I am an NLPer"
print(n_gram(sentence, 2))
print(n_gram(sentence.split(" "), 2))

