from sec41 import read

def sec46(chunks):
    res = ""
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
                    s.append(morph.base)
                    phrases.append(chunks[i].phrase())
            

        # 係っている格が存在する
        if len(s) > 0:
            res += "%s\t%s\t%s\n" % (verb.base, " ".join(s), " ".join(phrases))
    return res

sentences = read()
print(sec46(sentences[5]))

f = open("sec46.txt", "w")
for chunks in sentences:
    f.write(sec46(chunks))
