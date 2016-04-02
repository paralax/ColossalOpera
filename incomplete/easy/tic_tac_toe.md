# Title 

Winning in Tic Tac Toe

# Difficulty 

Easy

# Description

Welcome back! This is ESPN, broadcasting directly from Wembley Stadium, London! I'm /u/202halffound, and we're here to present you the Final Round of the Grand Finals of the XXVII Tic-Tac-Toe World Tournament. This is truly an incredible day for all fans of this ancient game. ... Now, it all boils down to this final move. Frank Giggs, the number 1 seed, has been thinking about this move for the past 10 minutes already. His clock is ticking down... he must make his move! Where is he going to place his piece...! 

# Input Description 

You will be given 4 lines of input via STDIN _or_ read from a file. The first line is a single character `X` or `O` which represents if it is x's turn to move or o's turn to move. The next 3 lines are three characters long and can be assumed to only contain the characters `X`, `O`, and `-`. These lines represent the Tic Tac Toe board. It can be assumed that the board is not already won. 

# Output Description

Output will be to STDOUT, _or_ displayed on the screen in a different way. If a winning move is available to the player who is currently moving, output the board with the winning move in place. Otherwise, output nothing. In the event that more than one winning move is available, either may be displayed. 

# Sample Input

Input:

    X 
    XX- 
    -XO 
    OO- 

Output: 

    XXX 
    -XO 
    OO- 

Input: 

    O 
    O-X 
    -OX 
    --- 

Output: 

    O-X 
    -OX 
    --O 

Input: 

    X 
    --O 
    OXX 
    --- 

Output: 

    (None)

# Bonus

This challenge was suggested by /u/202halffound. If you have an idea for a challenge, please share them on /r/dailyprogrammer_ideas.
