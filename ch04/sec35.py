from sec30 import read

sentences = read()

nouns = []

for sentence in sentences:
    noun = ""
    for morpheme in sentence:
        if morpheme['base'] == "*\n": continue
        if morpheme['pos'] == "名詞":
            noun += morpheme['base']
        else:
            if len(noun) > 0:
                nouns.append(noun)
            noun = ""

print(nouns)
