# Title

Hitori Solver

# Difficulty

Intermediate

# Description

Hitori is a logic puzzle similar to Soduku in that you aim to get unique digits in any column and row, but different in that you're given an *N*x*N* matrix and you have to knock out the flawed numbers. The rules (from [Wikipedia](http://en.wikipedia.org/wiki/Hitori)): "Hitori is played with a grid of squares or cells, and each cell contains a number. The objective is to eliminate numbers by filling in the squares such that remaining cells do not contain numbers that appear more than once in either a given row or column. Filled-in cells cannot be horizontally or vertically adjacent, although they can be diagonally adjacent. The remaining un-filled cells must form a single component connected horizontally and vertically." 

# Challenge Input

You'll be given an integer showing the number of rows and columns, then the board as a series of numbers, your program must output a board with the correct values removed (e.g. replaced with an X)

        8
        3 3 6 4 8 7 2 2 
        7 5 5 1 8 2 2 8
        4 7 4 5 6 1 8 2
        1 1 3 5 2 3 7 8
        2 8 8 3 1 4 6 5
        7 4 5 1 3 5 1 4
        8 5 7 2 4 5 2 3
        6 1 8 4 6 3 5 7
