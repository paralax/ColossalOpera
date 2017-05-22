# Title

Comparing Graphs

# Difficulty

Hard

# Tags

graph theory, edit distance

# Description

In mathematics and computer science, graph edit distance (GED) is a measure of similarity (or dissimilarity) between two graphs. The concept of graph edit distance was first formalized mathematically by Alberto Sanfliu and King-Sun Fu in 1983. The graph edit distance between two graphs is related to the string edit distance between strings. With the interpretation of strings as connected, directed acyclic graphs of maximum degree one, classical definitions of edit distance such as Levenshtein distance, Hamming distance and Jaro–Winkler distance may be interepeted as graph edit distances between suitably constrained graphs. Likewise, graph edit distance is also a generalization of tree edit distance between rooted trees.

To convert one graph into another, several different kinds of elementary graph operations are possible:

* vertex insertion to introduce a single new labeled vertex to a graph.
* vertex deletion to remove a single (often disconnected) vertex from a graph.
* vertex substitution to change the label (or color) of a given vertex.
* edge insertion to introduce a new colored edge between a pair of vertices.
* edge deletion to remove a single edge between a pair of vertices.
* edge substitution to change the label (or color) of a given edge.

As part of calculating the graph edit distance, each operation should have an associated non-zero cost. For today's challenge assume any of the above changes have a unit cost of 1, similar to the standard Levenshtein distance. 

Consider a pair of undirected graphs over two lines in `(i,j)` format for the nodes.

    (White, Black) (White, Maroon) (White, Red) (White, Pink) (White, Brown) (White, Orange) (White, Coral) (White, Olive) (Black, Maroon) (Black, Red) (Black, Pink) (Black, Brown) (Black, Orange) (Black, Coral) (Black, Olive) (Maroon, Red) (Maroon, Pink) (Maroon, Brown) (Maroon, Orange) (Maroon, Coral) (Maroon, Olive) (Red, Pink) (Red, Brown) (Red, Orange) (Red, Coral) (Red, Olive) (Pink, Brown) (Pink, Orange) (Pink, Coral) (Pink, Olive) (Brown, Orange) (Brown, Coral) (Brown, Olive) (Orange, Coral) (Orange, Olive) (Coral, Olive)
    (Hydrogen, Helium) (Hydrogen, Lithium) (Hydrogen, Beryllium) (Hydrogen, Boron) (Hydrogen, Carbon) (Hydrogen, Nitrogen) (Hydrogen, Oxygen) (Helium, Lithium) (Helium, Beryllium) (Helium, Boron) (Helium, Carbon) (Helium, Nitrogen) (Helium, Oxygen) (Lithium, Beryllium) (Lithium, Boron) (Lithium, Carbon) (Lithium, Nitrogen) (Lithium, Oxygen) (Beryllium, Boron) (Beryllium, Carbon) (Beryllium, Nitrogen) (Beryllium, Oxygen) (Boron, Carbon) (Boron, Nitrogen) (Boron, Oxygen) (Carbon, Nitrogen) (Carbon, Oxygen) (Nitrogen, Oxygen)

Your program should emit the GED calculated between the two graphs.
