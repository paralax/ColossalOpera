# Title

Singles

# Difficulty

Intermediate

# Tags

puzzle, game

# Description

[Singles](http://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/singles.html) is a number grid game where you must remove some squares in order to stabilize the grid. Black out some of the squares, in such a way that:

* no number appears twice in any row or column
* no two black squares are adjacent
* the white squares form a single connected group (connections along diagonals do not count).

# Input Description

You'll be given a single digit integer, *N*, on the first line. Then you'll be given an *N* x *N* grid of integers to play. Example:

    5
    3 2 2 1 3
    2 3 2 5 4
    4 5 2 2 1
    2 1 5 3 3
    5 3 1 3 5

# Challenge Output

Your program should emit the grid with the numbers you knock out (using the above rules) indicated, perhaps with an *x* marking where they were. Example:

    3 2 x 1 x
    x 3 2 5 4
    4 5 x 2 1
    2 1 5 x 3
    5 x 1 3 x

# Challenge Input

    8
    6 7 1 6 8 2 1 7
    2 8 5 7 6 4 6 1
    5 2 4 2 5 4 8 8
    5 3 8 2 6 1 4 7
    4 4 3 1 2 1 3 2
    6 2 3 5 8 2 7 8
    4 6 7 6 1 3 1 2
    8 8 1 4 1 6 2 2 

# Challenge Output 

    x 7 x 6 8 x 1 x
    2 8 5 7 x 4 6 1
    x 2 4 x 5 x 8 x
    5 3 8 2 6 1 4 7
    x 4 x 1 2 x 3 x
    6 x 3 5 x 2 7 8
    4 6 7 x 1 3 x 2
    8 x 1 4 x 6 2 x 
