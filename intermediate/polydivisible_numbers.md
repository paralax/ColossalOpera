# Title

Polydivisble Numbers

# Difficulty

Intermediate

# Description

In mathematics a polydivisible number is a number with digits *abcde*... that has the following properties :-

* Its first digit *a* is not 0.
* The number formed by its first two digits *ab* is a multiple of 2.
* The number formed by its first three digits *abc* is a multiple of 3.
* The number formed by its first four digits *abcd* is a multiple of 4.
* etc.

Your challenge today is to write a program that can generate one or more polydivisible numbers of a given length. 

# Input Description

You'll be given a single integer *N* on a line telling you how many digits long to generate a polydivisible number. Example:

    3

# Output Description

Your program should emit one or more polydivisible numbers for that length. Example:

    3 -> 246,249

# Challenge Input

    4
    5
    8

# Challenge Output

These are just some of the many polydivisible numbers. Your program may generate other valid ones. 

    4 -> 1020,1024
    5 -> 10205
    8 -> 10205448