# Title

4-Bit Mover-Robo Driver

# Difficulty

Intermediate

# Description

You're creating a driver for a mover robot, and it can only take input in one way--4-bit strings of 0's and 1's. The robot is designed to move about in a 5x5 2D grid and push blocks around. Given an input file describing instructions for the movement of the robot in this 4-bit string format, create a program to read in the input file and model the movement of the robot for the solution of pushing a single block off the grid given the initial state of the block being in the center, and the robot starting in the lower-left corner.
#Input

The input to the program should be a newline-delimited text file describing the moves the robot will take.

The format of the **character-encoded** file that holds binary input is as follows:

    NESW
    NESW
    NESW

Where N = north, E = east, S = south, and W = west, and each digit can either be 0 or 1. Only one of the four values can be '1'; else, the robot will not move; i.e.:

    0001 -> the robot will move west/left
    1010 -> the robot will not move
    0000 -> the robot will not move
    ABSC -> the robot will not move
    0801 -> the robot will not move
    *$&( -> the robot will not move
    00000001 -> the robot will not move, as there are 8 digits on a line

Each input comprises of a string of four binary digits followed by a newline, detailing the direction the robot will move next. If the square that the robot is trying to enter is occupied by a block, it will push the block in the direction it is headed. The robot can also push blocks outside of its 5x5 grid so that it "falls" off the platform; the robot should NOT be able to fall off the platform.

# Output

The output of the program should be a step-by-step simulation of your input, starting from right before the robot begins moving. The simulation should detail a solution of how to push a block out of the 5x5 2D grid, assuming the block is in the center and the robot starts in the lower-left corner:

    |_|_|_|_|_|
    |_|_|_|_|_|
    |_|_|O|_|_| 
    |_|_|_|_|_|
    |X|_|_|_|_|

         |
         V
    read input:
       1000
         |
         V

    |_|_|_|_|_|
    |_|_|_|_|_|
    |_|_|O|_|_| 
    |X|_|_|_|_|
    |_|_|_|_|_|

Represent the grid using pipes ('|') and underscores ('_'), representing the robot using a 'X' and the block using an 'O'.

The program will end once the block is pushed outside of the grid.

# Bonus

* Read input in a different format, such as hexadecimal or octal digits.
* Have the program check for errors in the input, using your own made-up convention (comments allowed or no comments? throw away non-conforming lines or still try to extract input from unfinished strings?).

# Credit

This challenge was created by /u/VermillionAzure. If you have any challenge ideas, please share them at /r/dailyprogrammer_ideas and there's a chance we'll use them!
