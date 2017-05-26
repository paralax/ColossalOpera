# Title

[2017-05-26] Challenge #316 [Hard] Longest Uncrossed Knight's Path

# Difficulty

Hard

# Tags

chess, graph theory

# Description

The longest uncrossed (or nonintersecting) knight's path is a mathematical problem involving a knight on the standard 8×8 chessboard or, more generally, on a square *n×n* board. The problem is to find the longest path the knight can take on the given board, such that the path does not intersect itself. A further distinction can be made between a closed path, which ends on the same field as where it begins, and an open path, which ends on a different field from where it begins.

For this challenge, assume the following: 

* You can make an open path
* You can start (and end) on any legal square
* Just like real chess, you're bounded by legal squares on the board
* The path is constructed from line segments between the start and end points of any of the knight's moves; intermediate squares it jumps over don't matter

This problem is intimately related to the knight's tour, a self-intersecting knight's path visiting all fields of the board. The key difference with this challenge is that the path may not intersect itself. Variants use fairy chess pieces like the camel ((3,1)-leaper), giraffe ((4,1)-leaper) and zebra ((3,2)-leaper) lead to problems of comparable complexity.

# Input Description

You'll be given the size *n* of the board representing the number of squares per side - it's a square board. Example:

    5

# Output Description

Your program should emit the length of the longest open tour, measured in line segments (e.g. moves). Example:

    10

# Challenge Input

    4
    7
    8

# Challenge Output

    5
    24
    35
