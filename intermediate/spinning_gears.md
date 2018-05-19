# Title

Spinning Gears

# Difficulty

Intermediate

# Tags

puzzle

# Description

A popular game for the babies of nerdy parents are wooden or plastic gears. Kids put them on a peg board (or use magnets to attach them to the refrigerator) and watch them spin. It's a simple way for them to learn about actions and interactions. As a parent, it was sometimes fun to see how big I could make the gear networks. There's a logic puzzle game I play on the iPad, too, to solve gear puzzles. 

Today's challenge is to read a set of gear specifications - their size and layout - and describe what initial gear to turn to make the target gear move in the right fashion - speed and direction. It's a bit of algebra and graph theory all thrown into one. You should assume frictionless gears. 

# Sample Input

You'll be given a line with a single integer on it (*N*) telling you how many gear specifications to read, followed by *N* lines. Gear specifications are given as a unique letter to designate it and then the radius of the gear. Then you'll be  given another link with a single integer on it (*M*) telling you the layout, showing you what gears are touching by their letters, followed by *M* lines. Finally, you'll be asked on the last line to spin a gear (designated by a letter) in a direction (clockwise (CW) or counter-clockwise (CCW)) and how fast in RPMs, ending with the name of the gear to turn. Example of 3 gears forming an A-B and B-C line, asking you to spin A to make C turn at 30 RPM counter clockwise:

    3 
    A 6
    B 12
    C 3
    2
    A B
    B C
    C CCW 30 A

# Sample Output

Your program should emit the gear name, direction (CW or CCW) and speed to make the target gear spin as needed. From our example:

    A CCW 15

# Challenge Input

    9
    A 6
    B 12
    C 3
    D 4
    E 5
    F 10
    G 15
    H 13
    I 9
    J 18
    15
    A B
    B B
    B C
    C A
    C A
    C B
    C B
    C B
    C C
    C I
    D B
    E B
    F B
    G B
    H B
    B CW 75 I
