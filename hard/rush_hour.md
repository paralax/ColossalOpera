# Title

Rush Hour Solver

# Difficulty

Hard

# Description

The game of Rush Hour is a puzzle game wherein the player has to slide the cars from their original position to allow the escape car to exit the board. Rush Hour is similar to other sliding puzzles, but with a twist: each piece moves along only one direction, instead of moving both horizontally and vertically. This makes individual moves easier to understand, and sequences easier to visualize. This is basically how cars move - forwards or backwards. 

Rush Hour includes a 6x6 playing board with an exit opening along on edge, a red escape car, and several blocking cars (of dimensions 2x1) and several blocking trucks (of dimensions 3x1 ).  The goal is to slide the red car (the escape vehicle) through the exit opening in the edge of the grid. To play, shift the cars and trucks up and down, left and right, until the path is cleared to slide the escape vehicle out the exit. You may not lift pieces off the grid. Pieces may only move forward and back, not sideways 

In this challenge you'll be given a starting layout, then you have to show how to move the cars to allow the red escape car to exit the board. 

# Sample Input

You'll be given the 6x6 (or 7x7) board, indicating the exit (with a `>`), along with the red escape car (marked with an `R`), and blocking cars (2x1 sized, indicated with letters `A` through `G`) and trucks (3x1 sized, indicated with letters `T` through `Z`). Empty spaces will be marked with a `.`. The way the cars are facing should be obvious from their orientation. Remember, they can only move forwards or backwards. Example:

    GAA..Y
    G.V..Y
    RRV..Y>
    ..VZZZ
    ....B.
    WWW.B.

# Sample Output

Find a solution to the puzzle, preferably one with the minimal number of steps. You should indicate which cars move in which direction to liberate the red escape car (`R`). From our example above here's a solution with `+` indicating to the right or down N squares, `-` indicating to the left or up N squares (plus or minus relative to a 0,0 cell in the top left corner):

    A +2 
    V -1
    Z -1
    Y +3
    R +5

# Challenge Input

    TTTAU.
    ...AU.
    RR..UB>
    CDDFFB
    CEEG.H
    VVVG.H

# Challenge Output

    R +1
    C -2
    D -1
    F -1
    U +3
    B -2
    R +4

Puzzles via http://www.puzzles.com/puzzlesineducation/plans/rushhourguide.pdf 
