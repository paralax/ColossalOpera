# Title

The Great Math Switch

# Difficulty

Intermediate

# Tags

math, puzzle

# Description

Imagine a switch that changes all the addition signs in an expression to multiplication signs, and all the subtraction signs to division signs. For example, if you had the expression 4 + 6 − 2, and you threw the switch, it would change to 4 * 6 / 2.

Your challenge today is to take a sequence of numbers and apply the right addition and subtraction symbols that, when flipped to multiplication and division symbols, yields the same answer. 

This challenge comes from Daniel Finkel of Math for Love, a Seattle-based math education consultancy, via [the Wordplay blog at the New York Times](http://wordplay.blogs.nytimes.com/2016/01/18/finkel-the-switch/). 

# Input Description

You'll be given a series of numbers, one per line, with blank symbols `_` between them. Example:

    1 _ 2 _ 3

# Output Description

Your program should emit the full equations, both sides of the switch, and show that they are equal. Example:

    1 + 2 + 3 = 1 * 2 * 3 = 6

# Challenge Input

    1 _ 2 _ 3 _ 4
    1 _ 2 _ 3 _ 4 _ 5 _ 6 _ 7
    1 _ 2 _ 3 _ 4 _ 5 _ 6 _ 7 _ 8 _ 9 _ 10

# Challenge Output

    1 - 2 + 3 + 4 = 1 / 2 * 3 * 4 = 8
    1 - 2 + 3 + 4 + 5 - 6 = 1 / 2 * 3 * 4 * 5 / 6 = 5
    1 - 2 + 3 + 4 - 5 + 6 + 7 - 8 - 9 + 10 = 1 / 2 * 3 * 4 ÷ 5 * 6 * 7 / 8 / 9 * 10 = 7
