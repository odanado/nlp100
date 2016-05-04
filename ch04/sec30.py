
def read():
    f = open("./neko.txt.mecab")
    sentence = []
    sentences = []
    
    for line in f:
        if line == "EOS\n":
            if len(sentence) > 0:
                sentences.append(sentence)
            sentence = []
        else:
            surface, features = line.split("\t")
            features = features.split(",")
            sentence.append({
                "surface": surface,
                "base": features[6],
                "pos": features[0],
                "pos1": features[1]
                })

    return sentences

if __name__ == "__main__":
    print(read())

