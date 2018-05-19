# Title

Zombies Invaded my Village

# Difficulty

Intermediate

# Tags

graph theory, math

# Description

(Read this in the tone of "Manic Pixie Dream Girls", the spirit in which it's intended.)

Help! Zombies invaded my village! I need your help to isolate them!

Let me describe my village. We have houses connected with paths between them, and that's how we get from one house to another. Sometimes I have to visit one house before I can get to another because I don't have a path from my house to that one, but that's OK. For example, I love walking past grandma's house, she always makes me rice pudding (yum!). 

But now zombies threaten our village. Our mayor, Francine, started to describe how to isolate the zombies by tearing up the paths and breaking the village into two parts. That means that some parts of the village will be turned into zombies, but thats better than the whole village being infected. (I hope grandma will be ok!) Before we could get to work, Francine was zombified, and now we're all left trying to figure out how to achieve her plan. She went to a really good university, and I am not that smart so I need your help!

What we want to do is to tell you about my village and have you tell me which paths to tear up and split our village into two parts so that we can defend it. We have to work fast so please tell me the minimum number of paths to tear up. 

Help us, DailyProgrammer, you're my only hope!

# Input Description

You'll be given a two integers on the first line, telling you how many lines to read (*N*) and how many distinct node IDs (*M*). Then you'll be given *N* lines of integers showing you the edge between the two nodes referenced by ID (1 -> *M*). Assume an edge weight of 1 and an undirected graph. Example:

    3
    1 2
    1 3
    2 3

# Output Description

Your program should emit the smallest number of edges to remove from the graph to split it into two. Example:

    1 2
    1 3

# Challenge Input

    89 18 14
    1 1 
    1 2 
    1 3 
    1 4 
    1 5 
    1 6 
    1 7 
    1 8 
    2 1 
    2 2 
    2 3 
    2 5 
    2 6 
    2 9 
    2 7 
    3 2 
    3 3 
    3 4 
    3 5 
    3 6 
    3 9 
    3 7 
    3 8 
    4 1 
    4 3 
    4 4 
    4 5 
    4 6 
    4 9 
    4 7 
    5 3 
    5 4 
    5 5 
    5 9 
    6 3 
    6 5 
    6 6 
    6 7 
    7 5 
    7 6 
    7 9 
    7 7 
    8 6 
    8 7 
    8 8 
    9 5 
    9 9 
    9 7 
    9 8 
    10 9 
    10 7 
    10 8 
    10 10 
    11 7 
    11 8 
    11 11 
    11 10 
    12 7 
    12 8 
    12 11 
    12 10 
    12 12 
    12 13 
    13 9 
    13 7 
    13 8 
    13 11 
    13 10 
    13 12 
    13 13 
    14 6 
    14 9 
    14 8 
    14 11 
    14 14 
    14 10 
    14 12 
    14 13 
    15 9 
    15 7 
    15 11 
    15 14 
    15 10 
    16 7 
    16 8 
    17 8 
    17 14 
    18 8 
    18 14 
