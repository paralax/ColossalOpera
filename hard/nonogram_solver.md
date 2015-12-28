# Title

Nonogram Solver

# Difficulty

Hard

# Tags

Nonogram, solver, puzzle, np-complete

# Description

Nonograms are picture logic puzzles in which cells in a grid must be colored or left blank according to numbers at the side of the grid to reveal a hidden picture. In this puzzle type, the numbers are a form of discrete tomography that measures how many unbroken lines of filled-in squares there are in any given row or column. For example, a clue of "4 8 3" would mean there are sets of four, eight, and three filled squares, in that order, with at least one blank square between successive groups.

The puzzles were invented in 1987 when Non Ishida, a Japanese graphics editor, won a competition in Tokyo by designing grid pictures using skyscraper lights that were turned on or off. Coincidentally, a professional Japanese puzzler named Tetsuya Nishio invented the same puzzles.

To solve a puzzle, one needs to determine which cells will be boxes and which will be empty. Determining which cells are to be left empty (called spaces) is as important as determining which to fill (called boxes). Later in the solving process, the spaces help determine where a clue (continuing block of boxes and a number in the legend) may spread. Simpler puzzles can usually be solved by a reasoning on a single row only (or a single column) at each given time, to determine as many boxes and spaces on that row as possible. Then trying another row (or column), until there are no rows that contain undetermined cells.

For more on Nonograms, see [Wikipedia](https://en.wikipedia.org/wiki/Nonogram). This challenge was inspired by a [blog post on the December 2015 GCHQ puzzle challenge](http://neilmitchell.blogspot.com/2015/12/solving-gchq-puzzle-by-hand.html). 

# Example Input

You'll be given a line with two integers telling you how many rows and columns (*n* x *m*) the puzzle contains. Then you'll be given the columns as numbers and the rows as numbers, along with the grid as dots `.` arranged in an *n* x *m* grid. Example showing a 4x4 grid:

    4 4    
          1 1  
        3 1 1 2 
      4 . . . .
    1 1 . . . .
      2 . . . .
      1 . . . .

# Example Output

Your program should emit a solution with the shaded cells marked with a pound sign `#`. Example:

    # # # #
    # . . #
    # # . .
    . . # .

# Challenge Input

    10 10
        4 6 8 8 8 8 8 8 6 4
    1 1 . . . . . . . . . .
    3 3 . . . . . . . . . .
     10 . . . . . . . . . .
     10 . . . . . . . . . .
     10 . . . . . . . . . .
     10 . . . . . . . . . .
      8 . . . . . . . . . .
      6 . . . . . . . . . .
      4 . . . . . . . . . .
      2 . . . . . . . . . .

# Challenge Output

    ..#....#..
    .###..###.
    ##########
    ##########
    ##########
    ##########
    .########.
    ..######..
    ...####...
    ....##....

(Yeah, this one was for fun.)
