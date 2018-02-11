# Title

Calculating Ulam Numbers

# Difficulty

Intermediate

# Description

Ulam numbers are a sequence of integers that are composed of previous, distinct members of the sequence that have exactly one possible representation of two previous Ulam numbers added together. Starting with U_1 = 1 and U_2 = 2, the next Ulam number is 3 (1+2), then 4 (1+3). 5 is not a Ulam number because it can be represented in two ways: 1+4 and 2+3. Through 100 the first few terms are

1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99

The sequence is named after the Polish physicist Stanislaw Ulam, who introduced it in 1964. There are infinitely many Ulam numbers. For, after the first n numbers in the sequence have already been determined, it is always possible to extend the sequence by one more element. 

Different sequences can be generated if U_1 and U_2 differ but the same rules apply. For example, for (1, 3) the sequence starts 1, 3, 4, 5, 6, 8, 10, 12, 17, 21, ...

# Input Description

You'll be given 2 integers representing U_1 and U_2. Example:

    1 2

# Output Description

Your program should emit the first 10 or so terms of the sequence for the given U starting values Example:

    1, 2, 3, 4, 6, 8, 11, 13, 16, 18

# Challenge Input

    2 5
    1 5
    3 7

# Challenge Output

