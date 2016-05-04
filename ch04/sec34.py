from sec30 import read

sentences = read()

noun_phrase = []

for sentence in sentences:
    for i in range(len(sentence)):
        if i == 0 or i + 1 == len(sentence): continue
        if sentence[i-1]['pos'] != "名詞" or sentence[i+1]['pos'] != "名詞": continue
        if sentence[i-1]['base'] == "*\n" or sentence[i+1]['base'] == "*\n": continue
        if sentence[i]['base'] == "の":
            noun_phrase.append(sentence[i-1]['base'] + sentence[i]['base'] + sentence[i+1]['base'])

print(noun_phrase)

