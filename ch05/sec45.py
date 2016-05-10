from sec41 import read

def sec45(chunks):
    for chunk in chunks:
        verb = [morph for morph in chunk.morphs if morph.pos == "動詞"]
        if len(verb) == 0: continue
        verb = verb[0]
        morphs = [chunks[i].morphs for i in chunk.srcs]
        s = []
        
        for i in chunk.srcs:
            s.append(" ".join([morph.base for morph in chunks[i].morphs if morph.pos == "助詞"]))

        print("%s\t%s" % (verb.base, " ".join(s)))

sentences = read()
chunks = sentences[5]
sec45(chunks)
