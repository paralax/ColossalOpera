# Title  

Wedderburn-Etherington Sequence

# Difficulty 

Easy

# Tags

integer sequence, infinite sequence, math, number theory

# Description

The Wedderburn-Etherington numbers are an integer sequence named for Ivor Malcolm Haddon Etherington and Joseph Wedderburn that can be used to count certain kinds of binary trees. The first few numbers in the sequence are

    0, 1, 1, 1, 2, 3, 6, 11, 23, 46, 98, 207, 451 ...
    
The Wedderburnâ–Etherington numbers may be calculated using the recurrence relation (in LaTeX notation)

    a_{2n-1} = \sum\limits{i=1}^n-1 a_ia_{2n-i-1}

    a_{2n} = a_n(a_n+1)/2 + \sum\limits{i=1}^n-1 a_ia_{2n-i}

See Wikipedia for more on the [Wedderburn-Etherington number](http://en.wikipedia.org/wiki/Wedderburn%E2%80%93Etherington_number) and its uses. 
 
# Input Description

You'll be given a number *n*, the number in the sequence to generate.

# Output Description

A sequence of integers in the Wedderburn-Etherington sequence up to position *n*.
