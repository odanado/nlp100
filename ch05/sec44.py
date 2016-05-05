import pydot.pydot as pydot
from sec41 import read

sentences = read()

chunks = sentences[7]
edges = []

for chunk in chunks:
    dst = chunk.dst
    if dst != -1:
        edges.append((chunk.phrase(), chunks[dst].phrase()))

g = pydot.graph_from_edges(edges)
g.write_jpeg('graph.jpg', prog='dot') 

