# Title

Tallest Tower from a List of Digits

# Difficulty

Intermediate

# Tags

ASCII art

# Description

Today we're building towers of digits. A digit can be on top of another one:

    2
    6

or can be supported by two other diagonally below it:

     9
    5 8

The bottom one(s) have to support the weight the upper one supports (if there is any), plus the upper one's weight which is always 1. If there are two supporters, they split the upper one's total weight evenly (50%-50%).

The weight of every digit is 1 independent of it's value. If one digit supports two others it has to be able to support the sum of their corresponding weight. A digit can support at most its numerical value.

Example valid towers look like this:

    7
    5
    2
    3

      1
     5 4
    5 9 5

# Input Description

You'll be given a list of space-separated integers, one list per line. Example:

    1 2 3 4 5

# Output Description

Your program should emit the maximal height of the tower you calculated and draw it, as well. Example:

    1 2 3 4 5 -> 5
    1
    2
    3
    4 
    5

# Challenge Input

    1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
    0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9
    0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 6 6 6 6 6 7 7 7 7 7 8 8 8 8 8 9 9 9 9 9

# Challenge Output

    1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 -> 9
       1
       2
       2
       3
       4
       5
      3 3
     4 4 4
    5 5 5 5

    0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 -> 12
     0
     1
     2
     3
     4
     5
     6
     7
    4 5
    6 7
    8 8
    9 9

    0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 6 6 6 6 6 7 7 7 7 7 8 8 8 8 8 9 9 9 9 9 -> 18
          0
          1
          2
          3
          4
          5
          6
          7
          8
          9
         5 5
         6 6
         7 7
        4 8 4
       3 7 7 3
      2 6 8 6 2
     2 5 8 8 5 2
     3 9 9 9 9 3
