from sec30 import read

sentences = read()
verbs = []

for sentence in sentences:
    verbs.extend([x['surface'] for x in sentence if x['pos'] == "動詞"])

print(verbs)
