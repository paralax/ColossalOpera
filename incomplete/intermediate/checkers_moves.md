# Title

Checkers Moves

# Difficulty

Intermediate

# Description

In checkers (or draughts as the Brits call it) you can move your pieces in onw of two ways: by sliding diagonally to an open square of the same color you're on, or by jumping a piece diagonnally to an open square. If the piece you jump is your opponent's, that's a *capture* to boot.

# Input Description

You'll be given a board in a piece of ASCII art. While there will be no labels, you should emit solutions marking rows as numbers and columns as letters, with `a1` in the lower left corner. You'll be given pieces as lowercase `o`s or `x`s to mark the two colors. Here's an example board showing an opening. 

    o - o - o - o -
    - o - o - o - o
    o - o - o - o -
    - - - - - - - -
    - - - - - - - -
    - x - x - x - x
    x - x - x - x -
    - x - x - x - x

# Output Description

Your program should emit the full set of moves possible for the board as given, with the piece type (`x` or `o`) and the source and destination squares. From the above example:

    THIS IS WRONG
    x b2 d1
    x b2 d3
    x c2 d1
    x c2 e

# Challenge Input

    o - o - o - - -
    - - - o - o - o
    o - o - o - o -
    - o - o - o - -
    x - x - x - x -
    - x - - - - - x
    x - - - - - x -
    - x - x - x - x

# Challenge Output
