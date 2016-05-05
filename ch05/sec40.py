# cat ./neko.txt | cabocha -f1 > neko.txt.cabocha

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "%s %s %s %s" % (self.surface, self.base, self.pos, self.pos1)

f = open("./neko.txt.cabocha")

sentences = []
sentence = []

for line in f:
    if line.startswith("* "): continue
    if line == "EOS\n":
        if len(sentence) > 0:
            sentences.append(sentence)
        sentence = []
    else:
        surface, features = line.split("\t")
        features = features.split(",")
        morph = Morph(surface, features[6], features[0], features[1])
        sentence.append(morph)

for morph in sentences[2]:
    print(str(morph))


