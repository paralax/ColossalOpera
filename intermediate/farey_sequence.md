# Title

Calculating the Farey Sequence

# Difficulty

Intermediate 

# Tags

number theory, sequence, rational numbers, fractions

# Description

In mathematics, the Farey sequence of order n is the sequence of completely reduced fractions between 0 and 1 which when in lowest terms have denominators less than or equal to n, arranged in order of increasing size.

Each Farey sequence starts with the value 0, denoted by the fraction 0/1, and ends with the value 1, denoted by the fraction 1/1 (although some authors omit these terms).

The first few entries of Farey sequence look like the following:

- F_1 = {0/1, 1/1}
- F_2 = {0/1, 1/2, 1/1}
- F_3 = {0/1, 1/3, 1/2, 2/3, 1/1}

#  Input Description

You'll be given a number *N*, one per line, telling you how many entries of the Farey sequence to generate. Example:

    4

#  Output Description

Your program should emit the sequence as a series of fractions of ascending value. Example:

    0/1 1/4 1/3 1/2 2/3 3/4 1/1

# Challenge Input

    11

# Challenge Output

(With line breaks for legibility)

    0/1 1/11 1/10 1/9 1/8 1/7 1/6 2/11 1/5 2/9 1/4 3/11 2/7 3/10 1/3 4/11 
    3/8 2/5 3/7 4/9 5/11 1/2 6/11 5/9 4/7 3/5 5/8 7/11 2/3 7/10 5/7 8/11 
    3/4 7/9 4/5 9/11 5/6 6/7 7/8 8/9 9/10 10/11 1/1