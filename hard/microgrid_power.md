# Title

Severing the Power Grid

# Difficulty

Hard

# Description

In energy production, the power grid is a a large directed graph of energy consumers and producers. At times you need to cut at certain nodes and trim demand because you cannot supply enough of a load. 

In DailyProgrammeropolis, all buildings are connected to the grid and all consume power to varying degrees. Some generate power because they have installed on-site generation and sell the excess to the grid, some do not.

The scenario you're facing is this: due to a fault with the bulk power generation facility not local to DailyProgrammerololis, you must trim the power grid. You have connectivity data, and power consumption and production data. Your goal with this challenge is to **maximize the number of powered nodes with the generated energy you have**. Note that when you cut off a node, you run the risk the downstream ones will loose power, too, if they are no longer connected. This is how you'll shed demand, by selectively cutting the graph. You can make as many cuts as you want (there is no restriction on this). 

# Input Description

You'll be given an extensive set of data for this challenge. The first set of data looks like this: you'll be given a single integer on one line telling you how many nodes to read. Then you'll be given those nodes, one per line, with the node ID, the amount of power it consumes in kWH, then how much the node generates in kWH. Not all nodes produce electricity, but some do (e.g. a wind farm, solar cells, etc), and there is obviously one that generates the most - that's your main power plant.

The next set of data is the edge data. The first line is how many edges to read, then the next *N* lines have data showing how the nodes are connected (e.g. power flows from node a to b). 

Example:

    3
    0 40.926 0.0
    1 36.812 1.552
    2 1.007 0.0
    2
    0 1
    0 2

# Challenge Input

    101
    0 1.926 0.0
    1 36.812 0.0
    2 1.007 0.0
    3 6.812 0.0
    4 1.589 0.0
    5 1.002 0.0
    6 1.531 0.0
    7 2.810 0.0
    8 1.246 0.0
    9 5.816 0.0
    10 1.167 0.0
    11 1.357 0.0
    12 1.585 0.0
    13 1.117 0.0
    14 3.110 1.553
    15 2.743 0.0
    16 1.282 0.0
    17 1.154 0.0
    18 1.160 0.0
    19 1.253 0.0
    20 1.086 0.0
    21 1.148 0.0
    22 1.357 0.0
    23 2.161 0.0
    24 1.260 0.0
    25 2.241 0.0
    26 2.970 0.0
    27 6.972 0.0
    28 2.443 0.0
    29 1.255 0.0
    30 1.844 0.0
    31 2.503 0.0
    32 1.054 0.0
    33 1.368 0.0
    34 1.011 1.601
    35 1.432 0.0
    36 1.061 1.452
    37 1.432 0.0
    38 2.011 0.0
    39 1.232 0.0
    40 1.767 0.0
    41 1.590 0.0
    42 2.453 0.0
    43 1.972 0.0
    44 1.445 0.0
    45 1.197 0.0
    46 2.497 0.0
    47 3.510 0.0
    48 12.510 0.0
    49 3.237 0.0
    50 1.287 0.0
    51 1.613 0.0
    52 1.776 0.0
    53 2.013 0.0
    54 1.079 0.0
    55 1.345 1.230
    56 1.613 0.0
    57 2.243 0.0
    58 1.209 0.0
    59 1.429 0.0
    60 7.709 0.0
    61 1.282 8.371
    62 1.036 0.0
    63 1.086 0.0
    64 1.087 0.0
    65 1.000 0.0
    66 1.140 0.0
    67 1.210 0.0
    68 1.080 0.0
    69 1.087 0.0
    70 1.399 0.0
    71 2.681 0.0
    72 1.693 0.0
    73 1.266 0.0
    74 1.234 0.0
    75 2.755 0.0
    76 2.173 0.0
    77 1.093 0.0
    78 1.005 0.0
    79 1.420 0.0
    80 1.135 0.0
    81 1.101 0.0
    82 1.187 1.668
    83 2.334 0.0
    84 2.054 3.447
    85 1.711 0.0
    86 2.083 0.0
    87 2.724 0.0
    88 1.654 0.0
    89 1.608 0.0
    90 1.033 17.707
    91 1.017 0.0
    92 1.528 0.0
    93 1.278 0.0
    94 1.128 0.0
    95 1.508 1.149
    96 5.123 0.0
    97 2.000 0.0
    98 1.426 0.0
    99 1.802 0.0
    100 2.995 98.606

Edge data is too much to put up here. You can download it [here](https://github.com/paralax/ColossalOpera/blob/master/hard/microgrid_edges.txt).

# Node data generation (Python)

    import random

    ALPHA=3
    CHANCE=0.05

    r2 = ALPHA
    for i in xrange(100):
        r1 = random.paretovariate(r2)
        r2 = random.paretovariate(r1)
        if random.random() < CHANCE:
            print "%s %.3f %.3f" % (i, r1, r2)
        else:
            print "%s %.3f 0.0" % (i, r1)

# Edge data generation (Python)

    import networkx as nx
    import random

    G=nx.gnp_random_graph(101,0.12,directed=True)
    DAG = nx.DiGraph([(u,v,{'weight':random.randint(-10,10)}) for (u,v) in G.edges() if u>v])
    with open('/tmp/edges', 'w') as f:
        for k,v in DAG.edges():
            f.write("%s %s\n" % (k,v))
