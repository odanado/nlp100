from sec41 import read

def sec45(chunks):
    res = ""
    for chunk in chunks:
        verb = [morph for morph in chunk.morphs if morph.pos == "動詞"]
        if len(verb) == 0: continue
        verb = verb[0]
        morphs = [chunks[i].morphs for i in chunk.srcs]
        s = []
        
        for i in chunk.srcs:
            for morph in chunks[i].morphs:
                if morph.pos == "助詞":
                    s.append(morph.base)

        # 係っている格がないなら何もしない
        if len(s) > 0:
            res += "%s\t%s\n" % (verb.base, " ".join(s))

    return res

sentences = read()
print(sec45(sentences[5]))

f = open("sec45.txt", "w")

for chunks in sentences:
    f.write(sec45(chunks))

