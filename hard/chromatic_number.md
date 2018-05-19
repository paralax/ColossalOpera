# Title

Calculate Graph Chromatic Number

# Difficulty

Hard

# Tags

math, graph theory

# Description

The [chromatic number](http://mathworld.wolfram.com/ChromaticNumber.html) of a graph G is the *smallest* number of colors needed to color the vertices of G so that no two adjacent vertices share the same color. 

To color a given graph, their first step is to scour the graph for a structure called a “prism,” which consists of a pair of three-holes connected to each other via three paths.

Chudnovsky and colleagues have been doing some neat work in this space, and recently [celebrated some breakthroughs](https://www.quantamagazine.org/20151020-perfect-graph-coloring/#st_refDomain=t.co&st_refQuery=/7ghlXNoW1b) in coloring real-world graphs. 

An interesting application via [this page](http://www.geeksforgeeks.org/graph-coloring-applications/): *Akamai runs a network of thousands of servers and the servers are used to distribute content on Internet. They install a new software or update existing softwares pretty much every week. The update cannot be deployed on every server at the same time, because the server may have to be taken down for the install. Also, the update should not be done one at a time, because it will take a lot of time. There are sets of servers that cannot be taken down together, because they have certain critical functions. This is a typical scheduling application of graph coloring problem. It turned out that 8 colors were good enough to color the graph of 75000 nodes. So they could install updates in 8 passes.*

Your challenge today is to implement an algorithm that calculates the chromatic number of an undirected graph. A useful link: [Graph Coloring](https://en.wikipedia.org/wiki/Graph_coloring) on Wikipedia. 

# Input Description

You'll be given a row with a two integers *n* and *m* on it telling you how many nodes (n) and how many edges (m) to parse. Then you'll be given the edges as two integers per line telling you which nodes are connected. These graphs are *undirected*, meaning the two edges have no directionality. Example:

    10 15
    0 1
    0 4
    0 5
    1 2
    1 6
    2 3
    2 7
    3 8
    3 4
    4 9
    5 8
    5 7
    6 8
    6 9
    7 9

# Output Description

Your program should emit the minimal chromatic number of the graph. The example graph above is the well known [Petersen graph (GP(5,2))](http://mathworld.wolfram.com/PetersenGraph.html). The example output would be:

    3

# Challenge Input

    18 153
    0 1
    0 2
    0 3
    0 4
    0 5
    0 6
    0 7
    0 8
    0 9
    0 10
    0 11
    0 12
    0 13
    0 14
    0 15
    0 16
    0 17
    1 2
    1 3
    1 4
    1 5
    1 6
    1 7
    1 8
    1 9
    1 10
    1 11
    1 12
    1 13
    1 14
    1 15
    1 16
    1 17
    2 3
    2 4
    2 5
    2 6
    2 7
    2 8
    2 9
    2 10
    2 11
    2 12
    2 13
    2 14
    2 15
    2 16
    2 17
    3 4
    3 5
    3 6
    3 7
    3 8
    3 9
    3 10
    3 11
    3 12
    3 13
    3 14
    3 15
    3 16
    3 17
    4 5
    4 6
    4 7
    4 8
    4 9
    4 10
    4 11
    4 12
    4 13
    4 14
    4 15
    4 16
    4 17
    5 6
    5 7
    5 8
    5 9
    5 10
    5 11
    5 12
    5 13
    5 14
    5 15
    5 16
    5 17
    6 7
    6 8
    6 9
    6 10
    6 11
    6 12
    6 13
    6 14
    6 15
    6 16
    6 17
    7 8
    7 9
    7 10
    7 11
    7 12
    7 13
    7 14
    7 15
    7 16
    7 17
    8 9
    8 10
    8 11
    8 12
    8 13
    8 14
    8 15
    8 16
    8 17
    9 10
    9 11
    9 12
    9 13
    9 14
    9 15
    9 16
    9 17
    10 11
    10 12
    10 13
    10 14
    10 15
    10 16
    10 17
    11 12
    11 13
    11 14
    11 15
    11 16
    11 17
    12 13
    12 14
    12 15
    12 16
    12 17
    13 14
    13 15
    13 16
    13 17
    14 15
    14 16
    14 17
    15 16
    15 17
    16 17

# Challenge Output

The smallest I can get is 16 colors (e.g. every node has an independent color). 
