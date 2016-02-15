# Title

Nurikabe Puzzle Solver 

# Difficulty

Hard

# Tags

puzzle, Nurikabe

# Description

A “nurikabe” is a kind of Japanese spirit that manifests as a wall that impedes or misdirects walking travelers at night. To solve a Nurikabe puzzle, paint some cells black, representing “ocean,” leaving the remaining cells white, representing “islands.” Island cells connect left/right and up/down, but not diagonally. The same is true of ocean cells. Each island must contain exactly one numbered cell, which describes its area in number of cells. When the puzzle is done, all the ocean cells must be connected. No 2 x 2 cells can be completely ocean (although they can be completely island).

For today's challenge you'll be asked to write a program that can solve a Nurikabe puzzle.

The [Wikipedia page on Nurikabe](https://en.wikipedia.org/wiki/Nurikabe_\(puzzle\)) is pretty good and includes a solution strategy you may want to implement. 

# Input Description

You'll be given given a row with a number *N*, telling you how many grid columns and rows there are - the grid is a square. Then you'll be given a the grid with empty cells indicated with an underscore `_` and the number squares indicated, as well. A squared marked with a `1` is a gimme. Example:

    6
    _ 1 _ _ _ _
    _ _ _ 4 _ _
    _ 3 _ _ _ _
    5 _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ 2

# Output Description

Your program should emit the puzzle as ASCII art with the open squares marked with an underscore `_` and the filled squares with a hash mark `#`. Example:

    # 1 # # # #
    # # # 4 _ #
    # 3 _ # _ #
    5 # _ # _ #
    _ # # # # #
    _ _ _ # _ 2

# Challenge Input

    8
    _ _ 2 _ 1 _ _ 6
    _ _ _ _ _ 1 _ _ 
    _ 2 _ _ _ _ _ _
    _ _ _ _ _ _ _ _
    _ _ _ _ _ _ _ _
    _ _ _ _ _ _ 3 _ 
    _ _ 1 _ _ _ _ _
    9 _ _ 1 _ 2 _ _ 

# Output Description

    # _ 2 # 1 # # 6
    # # # # # # 1 #
    _ 2 # _ # # # _
    # # # _ # _ _ _
    _ _ _ _ # # # #
    _ # # # _ _ 3 #
    _ # 1 # # # # #
    9 # # 1 # 2 _ #

via http://wordplay.blogs.nytimes.com/2016/01/18/finkel-the-switch/#more-104056
