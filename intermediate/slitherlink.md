# Title

Slitherlink

# Difficulty

Intermediate

# Description

Slitherlink is a logic puzzle that was first published by Nikoli in Japan. The puzzle consists of a grid of dots, with some clue cells containing numbers. You connect horizontally or vertically adjacent dots to form a meandering path that forms a single loop or "Slitherlink." The loop must not have any branches and must not cross itself. The clue numbers indicate how many lines surround the cell. Empty cells may be surrounded by any number of lines (from 0 to 3). 

Remember, the three rules for Slitherlink are:

1. Connect dots with vertical / horizontal line and make one loop,
2. Numbers are the hints to know how many lines can be drawn around it. There may be any number of lines around cells without number,
3. Lines cannot be crossed or branch off.

A simple example would be like this:

    + + + +     +-+-+-+ 
     3 2 3  =>  |3 2 3|    
    + + + +     +-+-+-+ 

Using dashes `-` and pipes `|` draw the lines to connect the dots. 

# Input Description

You'll be given a square of numbers and nodes. The numbers indicate the square and the dots are represented by the `+` sign. Some squares may be blank, that's a wildcard. Example:

    + + + + +
     1 0   1
    + + + + +
     3 3
    + + + + +
         2 2
    + + + + +
     3   1 0 
    + + + + +

# Output Description

You should link the dots with a dash `-` or a pipe `|` as needed to satisfy the puzzle. Example:

    + + + + +
     1 0   1
    +-+ +-+-+
    |3|3|   |
    + +-+ +-+
    |    2|2
    + +-+-+ +
    |3|  1 0 
    +-+ + + +

# Challenge Input

    + + + + + + + + +
     0 2 3 3 3 2 2 3
    + + + + + + + + +
     2             3
    + + + + + + + + +
     2 2 3         3
    + + + + + + + + +
         1
    + + + + + + + + +
               3
    + + + + + + + + +
     0         0 2 2
    + + + + + + + + +
     2             1
    + + + + + + + + +
     3 1 1 3 2 2 3 1
    + + + + + + + + +

# Challenge Output

    + + +-+ +-+ +-+-+
     0 2|3|3|3|2|2 3|
    + +-+ +-+ + + +-+
     2|       | | |3
    +-+ +-+ + +-+ +-+
    |2 2|3|        3|
    + +-+ + +-+-+-+-+
    | |  1| |
    +-+ + + + +-+ +-+
          | | |3| | |
    + + +-+ +-+ +-+ +
     0  |      0 2 2|
    + +-+ +-+-+ +-+-+
     2|   |   | |  1
    +-+ + +-+ + +-+ +
    |3 1 1 3|2|2 3|1
    +-+-+-+-+ +-+-+ +

# Credit

This puzzle cam from the New York Times magazine on May 24, 2015. You can find more slitherlink puzzles on this website: http://krazydad.com/slitherlink/



http://www.kakuro-online.com/slitherlink/
