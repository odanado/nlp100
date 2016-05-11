from sec41 import read

def sec46(chunks):
    for chunk in chunks:
        verb = [morph for morph in chunk.morphs if morph.pos == "動詞"]
        if len(verb) == 0: continue
        verb = verb[0]
        morphs = [chunks[i].morphs for i in chunk.srcs]
        s = []
        phrases = []
        
        for i in chunk.srcs:
            for morph in chunks[i].morphs:
                if morph.pos == "助詞":
                    s.append(" ".join(morph.base))
                    phrases.append(chunks[i].phrase())
            

        print("%s\t%s\t%s" % (verb.base, " ".join(s), " ".join(phrases)))

sentences = read()
chunks = sentences[5]
sec46(chunks)
