from sec41 import read

sentences = read()

for chunks in sentences:
    for chunk in chunks:
        if "名詞" in [morph.pos for morph in chunk.morphs]:
            dst = chunk.dst
            if "動詞" in [morph.pos for morph in chunks[dst].morphs]:
                print("%s\t%s" % (chunk.phrase(), chunks[dst].phrase()))
