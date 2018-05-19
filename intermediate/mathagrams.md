# Title 

Mathagrams

# Difficulty 

Intermediate 

# Tags

math, puzzle, game

# Description

A mathagram is a puzzle where you have to fill in the unknown digits to arrive at a given sum, with the values being added using every digit between 1 and 9 exactly once (yielding three 3-digit numbers). For this challenge, you'll write a program to solve such puzzles. 

# Input Description

You'll be given a simple addition equation and the sum to arrive at, with the letter *x* in place of the unknown digit for you to fill it. Example:

        1xx + xxx = 468

# Output Description

Emit the filled in equation with the *x* placeholders replaced by digits, making sure the addition adds up to the stated sum.  Example: 

        193 + 275 = 468

# Challenge Input

        xx5 + xxx = 468
        x9x + xxx = 468
        xxx + x7x = 468

# Challenge Output

        175 + 293 = 468
        195 + 273 = 468
        295 + 173 = 468
