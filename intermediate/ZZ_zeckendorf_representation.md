# Title

[2016-10-05] Challenge #286 [Intermediate] Zeckendorf Representations of Positive Integers

# Difficulty

Intermediate

# Tags

number theory

# Description

Zeckendorf's theorem, named after Belgian mathematician Edouard Zeckendorf, is a theorem about the representation of integers as sums of Fibonacci numbers.

Zeckendorf's theorem states that every positive integer can be represented uniquely as the sum of one or more distinct Fibonacci numbers in such a way that the sum does not include any two consecutive Fibonacci numbers. 

For example, the Zeckendorf representation of 100 is

    100 = 89 + 8 + 3

There are other ways of representing 100 as the sum of Fibonacci numbers – for example

    100 = 89 + 8 + 2 + 1
    100 = 55 + 34 + 8 + 3

but these are not Zeckendorf representations because 1 and 2 are consecutive Fibonacci numbers, as are 34 and 55.

Your challenge today is to write a program that can decompose a positive integer into its Zeckendorf representation.

# Sample Input

You'll be given a number *N* on the first line, telling you how many lines to read. You'll be given a list of *N* positive integers, one per line. Example:

    3
    4
    100
    30

# Sample Output

Your program should emit the Zeckendorf representation for each of the numbers. Example:

    4 = 3 + 1
    100 = 89 + 8 + 3 
    30 = 21 + 8 + 1

# Challenge Input

    5
    120
    34
    88
    90
    320

