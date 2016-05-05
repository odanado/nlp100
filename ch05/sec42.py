from sec41 import read

sentences = read()

for chunks in sentences:
    for chunk in chunks:
        phrases = chunk.phrase() + "\t"
        phrases += "\t".join([chunks[i].phrase() for i in chunk.srcs])
        print(phrases)
        
