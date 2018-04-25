# Title

Primes in Grids

# Difficulty

Easy

# Tags

prime numbers

# Description

This puzzle was first proposed (1989) by [Gordon Lee](http://www.primepuzzles.net/puzzles/puzz_001.htm): given a grid of numbers, how many *distinct* primes can you find embedded in the matrix, regarding that you can read the lines or part of them, in form vertical, horizontal or diagonal orientation, in both directions. 

Note that you can't change direction once you start moving (e.g. this isn't Boggle). 

# Input Description

You'll be given a single number on a line which tells you how many rows and columns to read (all grids will be square). Example:

    3 
    113
    754
    937

# Output Description

Your program should emit the number of distinct primes it finds in the grid. Optionally list them. Example:

    30
    113, 311, 179, 971, 157, 751 359, ...

# Challenge Input

    5 
    11933
    99563
    89417
    33731
    32939
    
    6
    317333
    995639
    118142
    136373
    349199
    379379

# Challenge Output

    116

    187
