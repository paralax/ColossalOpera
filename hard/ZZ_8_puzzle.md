# Title

8 Puzzle

# Difficulty

Hard

# Description

The 8-puzzle problem is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide blocks horizontally or vertically into the blank square. Here's an example showing some of the intermediate steps:


        1  3        1     3        1  2  3        1  2  3        1  2  3
     4  2  5   =>   4  2  5   =>   4     5   =>   4  5      =>   4  5  6
     7  8  6        7  8  6        7  8  6        7  8  6        7  8 

     initial                                                      goal

Write a program that reads the initial board and yields a sequence of board positions that solves the puzzle in the fewest number of moves. Also print out the total number of moves and the total number of states ever enqueued.

# Input Description

You'll be given the puzzle as a series of numbers and a blank. You can assume that it is a *3x3* grid and that you have (3*3)-1 (8) tiles. Example:

    7 5 6
    2 4 3
    1 8

# Output Description

Output the steps you took to get to the solution.

# Challenge Input

    8 7 6
    5 4 3
    2 1 

    5   3
    2 8 4
    6 7 1

