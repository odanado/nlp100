
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "%s %s %s %s" % (self.surface, self.base, self.pos, self.pos1)

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []
    
    def phrase(self):
        return "".join([morph.surface for morph in self.morphs])

def read():
    f = open("./neko.txt.cabocha")
    sentences = []
    chunks = []
    morphs = []
    dst = -1
    for line in f:
        if line == "EOS\n":
            if len(morphs) > 0:
                chunks.append(Chunk(morphs, dst))
            if len(chunks) > 0:
                sentences.append(chunks)
            chunks = []
            morphs = []
        elif line.startswith("* "):
            if len(morphs) > 0:
                chunks.append(Chunk(morphs, dst))
            morphs = []
            dst = line.split()[2]
            dst = int(dst[:-1])
        else:
            surface, features = line.split("\t")
            features = features.split(",")
            morphs.append(Morph(surface, features[6], features[0], features[1]))


    for chunks in sentences:
        for i in range(len(chunks)):
            dst = chunks[i].dst
            chunks[dst].srcs.append(i)

    return sentences

if __name__ == '__main__':
    sentences = read()

    chunks = sentences[7]
    for chunk in chunks:
        dst = chunk.dst
        print("%s -> %s" % (chunk.phrase(), chunks[dst].phrase()))

