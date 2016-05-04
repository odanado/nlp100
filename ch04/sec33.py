from sec30 import read

sentences = read()
nouns = []
for sentence in sentences:
    nouns.extend([x['base'] for x in sentence if x['pos'] == "名詞" and x['pos1'] == "サ変接続" and x['surface'] != "——"])

print(nouns)
