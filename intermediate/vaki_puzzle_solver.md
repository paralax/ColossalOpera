# Title

Vaki Puzzle Solver

# Difficulty

Intermediate

# Description

Vaki puzzles are solved by completing the grid so that there are two symbols in each cell (most commonly a letter and a number), each letter and each number appears once in each column and once in each row, and each pair appears only once in the grid. 

Vaki puzzles are solved by completing the grid so that there is a letter and a number and in each cell, each letter and each number appears once in each column and once in each row, and each pair appears only once in the grid.

For a little bit more, see [the Vaki Puzzle website](http://www.vakipuzzles.com/). 

# Input Description

On the first line you'll be given a single integer, *N*, which is the size of the grid to make (both in the horizontal and vertical axes, it's a square grid). Assume the numbers go from *1* to *N* and the letters from *A* to the *Nth* letter (e.g. C = 3, D = 4, etc). Subsequent lines will specify 3 values - two integers (row and column respectively) and one additional value, either a letter (e.g. *C_*), a number (e.g. *_2*), or a combination (e.g. *D1*). The "_" underscore means that there's a missing value.

# Output Description

You should emit a simple grid showing all positions filled in for a valid puzzle with those constraints. 

# Sample Input

        4
        1 2 D3
        4 4 C_
        2 3 _2

# Sample Output

        C2      D3      A1      B4
        D1      C4      B2      A3
        A4      B1      C3      D2
        B3      A2      D4      C1

# Notes

The basic ideas of a Soduku solver apply here, although at a different depth (3 fold compared to Soduku). 

