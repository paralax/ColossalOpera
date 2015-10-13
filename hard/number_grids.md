# Title

Number Grid Puzzles

# Difficulty

Hard

# Description

Imagine a grid of numbers, not unlike soduku. Your task is to place digits in them following some rules, but then it gets different than soduku. First, each row and column of the grid forms a multi-digit number. Second, each of those numbers must meet some specific properties. 

Today's challenge is to play those games. 

# Input Description

You'll be given the description of the puzzle on the first two lines. The first line of input has the size of the grid as *x* * *y*. The second line tells you what digits are available. Then the next x*y numbers tell you the row and column constraints. The language will be regular. Descriptions will be "col" or "row" for column or row, respectively, and then the number. Then the constrains of the row or column will be given. Choices will include "prime", "cube", or "multiple of N" where N is an integer. Example:

    2 2 
    1 2 3 4
    row 1 prime
    row 2 multiple of 8
    col 1 prime
    col 2 multiple of 4

# Output Description

Your program should emit a valid solution to the puzzle. From the above example:

    4 1
    3 2

This one works because both `41` and `43` are primes, `12` is a multiple of 4 and `32` is a multiple of 8. 

# Challenge Input

    3 3
    1 2 3 4 5 6 7 8 9
    row 1 even
    row 2 prime
    row 3 cube
    col 1 prime
    col 2 cube
    col 3 prime

    2 2
    1 3 5 7 
    row 1 prime
    row 2 prime
    col 1 prime
    col 2 prime

# Challenge Output

    4 5 8 
    6 1 3
    7 2 9

    NO SOLUTION

From http://chalkdustmagazine.com/regulars/puzzles/puzzles-on-square-grids/#more-1396 
