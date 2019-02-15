# Title

[2019-02-15] Challenge #375 [Hard] Graph of Thrones 

# Difficulty

Hard

# Tags

graph theory, math

# Description

We'll focus in this challenge on what's called a _complete graph_, wherein every node is expressly connected to every other node. We'll also work assuming an undirected graph, that relationships are reciprocal. 

In social network analysis, you can analyze for _structural balance_ - a configuration wherein you'll find local stability. The easy one is when everyone enjoys a positive relationship with everyone else - they're all friends. Another structurally balanced scenario is when you have - in a graph of three nodes - two friends and each with a shared enemy, so one positive relationship and two negative ones. 

With larger graphs, you can continue this analysis by analyzing every three node subgraph and ensuring it has those properties - all positive or one positive and two negative relationsgips. 

A structurally balanced graph doesn't indicate complete future stability, just local stability - remember, factions can arise in these networks, akin to the Axis and Allies scenario of WW1 and WW2. 

Today's challenge is to take a graph and identify if the graph is structurally balanced. This has great applicability to social network analysis, and can easily be applied to stuff like fictional universes like the Game of Thrones and the real world based on news events. 

# Example Input

You'll be given a graph in the following format: the first line contains two integers, _N_ and _M_, telling you how many nodes and edges to load, respectively. The next _M_ lines tell you relationships, positive (friendly, denoted by `++`) or negative (foes, denoted by `--`). Example (from a subset of the Legion of Doom and Justice League):

    6 15
    Superman ++ Green Lantern
    Superman ++ Wonder Woman
    Superman -- Sinestro
    Superman -- Cheetah
    Superman -- Lex Luthor
    Green Lantern ++ Wonder Woman
    Green Lantern -- Sinestro
    Green Lantern -- Cheetah
    Green Lantern -- Lex Luthor
    Wonder Woman -- Sinestro
    Wonder Woman -- Cheetah
    Wonder Woman -- Lex Luthor
    Sinestro ++ Cheetah
    Sinestro Lex ++ Luthor
    Cheetah Lex ++ Luthor

# Example Output

Your program should emit if the graph is structurally balanced or not. Example:

    balanced

# Challenge Input

This is the Game of Thrones Season 7 house list I found via [this list of alliances on the Vulture website](http://www.vulture.com/2017/08/game-of-thrones-season-7-alliances.html) - I don't watch GoT so I have no idea if I captured this right. 

    120 16
    Daenerys Targaryen ++ Jon Snow
    Daenerys Targaryen ++ Tyrion Lannister
    Daenerys Targaryen ++ Varys
    Daenerys Targaryen ++ Jorah Mormont
    Daenerys Targaryen ++ Beric Dondarrion
    Daenerys Targaryen ++ Sandor “the Hound” Clegane
    Daenerys Targaryen ++ Theon and Yara Greyjoy
    Daenerys Targaryen -- Sansa Stark
    Daenerys Targaryen -- Arya Stark
    Daenerys Targaryen -- Bran Stark
    Daenerys Targaryen -- The Lords of the North and the Vale
    Daenerys Targaryen -- Littlefinger
    Daenerys Targaryen -- Cersei Lannister
    Daenerys Targaryen -- Jaime Lannister
    Daenerys Targaryen -- Euron Greyjoy
    Jon Snow ++ Tyrion Lannister
    Jon Snow ++ Varys
    Jon Snow ++ Jorah Mormont
    Jon Snow ++ Beric Dondarrion
    Jon Snow ++ Sandor “the Hound” Clegane
    Jon Snow -- Theon and Yara Greyjoy
    Jon Snow -- Sansa Stark
    Jon Snow -- Arya Stark
    Jon Snow -- Bran Stark
    Jon Snow -- The Lords of the North and the Vale
    Jon Snow -- Littlefinger
    Jon Snow -- Cersei Lannister
    Jon Snow -- Jaime Lannister
    Jon Snow -- Euron Greyjoy
    Tyrion Lannister ++ Varys
    Tyrion Lannister ++ Jorah Mormont
    Tyrion Lannister ++ Beric Dondarrion
    Tyrion Lannister ++ Sandor “the Hound” Clegane
    Tyrion Lannister ++ Theon and Yara Greyjoy
    Tyrion Lannister -- Sansa Stark
    Tyrion Lannister -- Arya Stark
    Tyrion Lannister -- Bran Stark
    Tyrion Lannister -- The Lords of the North and the Vale
    Tyrion Lannister -- Littlefinger
    Tyrion Lannister -- Cersei Lannister
    Tyrion Lannister -- Jaime Lannister
    Tyrion Lannister -- Euron Greyjoy
    Varys ++ Jorah Mormont
    Varys ++ Beric Dondarrion
    Varys ++ Sandor “the Hound” Clegane
    Varys ++ Theon and Yara Greyjoy
    Varys -- Sansa Stark
    Varys -- Arya Stark
    Varys -- Bran Stark
    Varys -- The Lords of the North and the Vale
    Varys -- Littlefinger
    Varys -- Cersei Lannister
    Varys -- Jaime Lannister
    Varys -- Euron Greyjoy
    Jorah Mormont ++ Beric Dondarrion
    Jorah Mormont ++ Sandor “the Hound” Clegane
    Jorah Mormont ++ Theon and Yara Greyjoy
    Jorah Mormont -- Sansa Stark
    Jorah Mormont -- Arya Stark
    Jorah Mormont -- Bran Stark
    Jorah Mormont -- The Lords of the North and the Vale
    Jorah Mormont -- Littlefinger
    Jorah Mormont -- Cersei Lannister
    Jorah Mormont -- Jaime Lannister
    Jorah Mormont -- Euron Greyjoy
    Beric Dondarrion ++ Sandor “the Hound” Clegane
    Beric Dondarrion ++ Theon and Yara Greyjoy
    Beric Dondarrion -- Sansa Stark
    Beric Dondarrion -- Arya Stark
    Beric Dondarrion -- Bran Stark
    Beric Dondarrion -- The Lords of the North and the Vale
    Beric Dondarrion -- Littlefinger
    Beric Dondarrion -- Cersei Lannister
    Beric Dondarrion -- Jaime Lannister
    Beric Dondarrion -- Euron Greyjoy
    Sandor “the Hound” Clegane ++ Theon and Yara Greyjoy
    Sandor “the Hound” Clegane -- Sansa Stark
    Sandor “the Hound” Clegane -- Arya Stark
    Sandor “the Hound” Clegane -- Bran Stark
    Sandor “the Hound” Clegane -- The Lords of the North and the Vale
    Sandor “the Hound” Clegane -- Littlefinger
    Sandor “the Hound” Clegane -- Cersei Lannister
    Sandor “the Hound” Clegane -- Jaime Lannister
    Sandor “the Hound” Clegane -- Euron Greyjoy
    Theon and Yara Greyjoy -- Sansa Stark
    Theon and Yara Greyjoy -- Arya Stark
    Theon and Yara Greyjoy -- Bran Stark
    Theon and Yara Greyjoy -- The Lords of the North and the Vale
    Theon and Yara Greyjoy -- Littlefinger
    Theon and Yara Greyjoy -- Cersei Lannister
    Theon and Yara Greyjoy -- Jaime Lannister
    Theon and Yara Greyjoy -- Euron Greyjoy
    Sansa Stark ++ Arya Stark
    Sansa Stark ++ Bran Stark
    Sansa Stark ++ The Lords of the North and the Vale
    Sansa Stark ++ Littlefinger
    Sansa Stark -- Cersei Lannister
    Sansa Stark -- Jaime Lannister
    Sansa Stark -- Euron Greyjoy
    Arya Stark ++ Bran Stark
    Arya Stark ++ The Lords of the North and the Vale
    Arya Stark ++ Littlefinger
    Arya Stark -- Cersei Lannister
    Arya Stark -- Jaime Lannister
    Arya Stark -- Euron Greyjoy
    Bran Stark ++ The Lords of the North and the Vale
    Bran Stark -- Littlefinger
    Bran Stark -- Cersei Lannister
    Bran Stark -- Jaime Lannister
    Bran Stark -- Euron Greyjoy
    The Lords of the North and the Vale ++ Littlefinger
    The Lords of the North and the Vale -- Cersei Lannister
    The Lords of the North and the Vale -- Jaime Lannister
    The Lords of the North and the Vale -- Euron Greyjoy
    Littlefinger -- Cersei Lannister
    Littlefinger -- Jaime Lannister
    Littlefinger -- Euron Greyjoy
    Cersei Lannister ++ Jaime Lannister
    Cersei Lannister ++ Euron Greyjoy
    Jaime Lannister ++ Euron Greyjoy

# Notes

You can learn more about the ideas behind this challenge in these resources:

* [Positive and Negative Relationships](https://courses.cit.cornell.edu/info204_2007sp/balance.pdf), in D. Easley and J. Kleinberg. Networks, Crowds, and Markets: Reasoning about a Highly Connected World (2010). 
* [Network Mathematics and Rival Factions](https://www.youtube.com/watch?v=qEKNFOaGQcc) from the PBS Digital YouTube channel Infinite Series. It was this video that inspired this challenge. 
* [The Graph of Thrones \[Season 7 Contest\]](https://neo4j.com/blog/graph-of-thrones/), from the Neo4j site referencing how to use their software to answer a Kaggle challenge about predicting GoT's future. 
