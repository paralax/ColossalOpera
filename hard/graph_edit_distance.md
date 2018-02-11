# Title

Comparing Graphs

# Difficulty

Hard

# Tags

graph theory, edit distance

# Description

In mathematics and computer science, graph edit distance (GED) is a measure of similarity (or dissimilarity) between two graphs. The concept of graph edit distance was first formalized mathematically by Alberto Sanfliu and King-Sun Fu in 1983. The graph edit distance between two graphs is related to the string edit distance between strings. With the interpretation of strings as connected, directed acyclic graphs of maximum degree one, classical definitions of edit distance such as Levenshtein distance, Hamming distance and Jaro–Winkler distance may be interpreted as graph edit distances between suitably constrained graphs. Likewise, graph edit distance is also a generalization of tree edit distance between rooted trees.

To convert one graph into another, several different kinds of elementary graph operations are possible:

* vertex insertion to introduce a single new labeled vertex to a graph.
* vertex deletion to remove a single (often disconnected) vertex from a graph.
* vertex substitution to change the label (or color) of a given vertex.
* edge insertion to introduce a new colored edge between a pair of vertices.
* edge deletion to remove a single edge between a pair of vertices.
* edge substitution to change the label (or color) of a given edge.

As part of calculating the graph edit distance, each operation should have an associated non-zero cost. For today's challenge assume any of the above changes have a unit cost of 1, similar to the standard Levenshtein distance. 

Consider a pair of undirected graphs over two lines in `(i,j)` format for the nodes.

    (White, Black) (White, Maroon) (White, Red) (Black, Maroon) (Black, Red) (Maroon, Red)
    (White, Black) (White, Maroon) (White, Red) (White, Pink) (Black, Maroon) (Black, Red) (Black, Pink) (Maroon, Red) (Maroon, Pink) (Red, Pink)

Your program should emit the GED calculated between the two graphs.
