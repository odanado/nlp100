from sec41 import read

def get_sa_noun(morphs):
    for morph in morphs:
        if morph.pos1 == "サ変接続":
            return morph
    return None

def sec47(chunks):
    res = ""
    for chunk in chunks:
        verb = [morph for morph in chunk.morphs if morph.pos == "動詞"]
        if len(verb) == 0: continue
        verb = verb[0].base
        s = []
        phrases = []
        exist_sa_noun = False

        for i in chunk.srcs:
            for morph in chunks[i].morphs:
                if morph.pos == "助詞":
                    sa_noun = get_sa_noun(chunks[i].morphs)
                    if morph.base == "を" and sa_noun != None:
                        verb = sa_noun.base + verb
                        exist_sa_noun = True
                    else:
                        s.append(morph.base)
                        phrases.append(chunks[i].phrase())
                    break
            

        # 係っている格が存在する
        if len(s) > 0 and exist_sa_noun:
            res += "%s\t%s\t%s\n" % (verb, " ".join(s), " ".join(phrases))
    return res

sentences = read()
print(sec47(sentences[868]))

f = open("sec47.txt", "w")
for chunks in sentences:
    f.write(sec47(chunks))

# cat sec47.txt | cut -f1 | sort | uniq -c | sort
