# Title

[2017-08-18] Challenge #327 [Hard] Calculating Costas Arrays

# Difficulty

Hard

# Tags

computer graphics, permutation arrays

# Description

Costas arrays are special permutation matrices.  A permutation matrix contains 0s and 1s such that each row and each column contains only a single 1. The identity matrix is a trivial example:

    1 0 0
    0 1 0
    0 0 1

The special property of Costas arrays are that the distance between any pair of ones in the matrix is not repeated for another pair of ones. This means that the identity matrix is _not_ a valid Costas array because each closest pair of 1s is the same distance apart. 

Costas arrays are named after John P. Costas, who first wrote about them in a 1965 technical report.

Costas arrays have a number of applications. This property was originally defined to make the permutation matrix an optimal scheme for setting frequencies in a multiple-tone sonar waveform because it means that unless the receiver is locked on the signal in both frequency and time, no more than one tone will be where it is expected. This property also makes Costas arrays ideal for one of the techniques in sophisticated communications and radar waveforms. 

Furthermore, Costas arrays are an active area of research in computer graphics.

Costas arrays have an order _N_ which describes the length of one of their sides; they are squares.

Today's challenge is to calculate the number of Costas arrays given an order. 

# Input Description

You'll be given a number _N_, one integer per line, telling you the order of the Costas array. Example:

    3
    5

# Output Description

Your program should emit the number of distinct Costas arrays for that order. From our example:

    3 -> 4
    5 -> 40

# Challenge Input

    6
    7
    13

# Challenge Output

    6 -> 116
    7 -> 200
    13 -> 12828

Orders 13-18 should test the efficiency of your solution pretty well.
