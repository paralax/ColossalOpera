# Title

Van der Waerden numbers

# Difficulty

Hard

# Tags

number theory, coloring, Ramsey theory, math

# Description

This one came to me via the always interesting [Data Genetics blog](http://datagenetics.com/blog/august12017/index.html). 

Van der Waerden's theorem relates to ways that collections can be colored, in order, avoiding spacing of colors that are a defined length arithmetic progression apart. They are named after the Dutch mathematician B. L. van der Waerden. _W(c,k)_ can be defined as the smallest value where c represents the number of colors in the sequence, and k represents the number of elements in the arithmetic progression.

In mathematics, an arithmetic progression is a sequence of numbers such that the difference between the consecutive terms is constant. For instance, the sequence 5, 7, 9, 11, 13, 15, ... is an arithmetic progression with common difference of 2.

[Van der Waerden numbers](https://en.wikipedia.org/wiki/Van_der_Waerden_number) (W) are defined as the smallest arrangement of _c_ different colors such that there exists an arithmetic sequence of length _k_. The simplest non-trivial example is _W(2,3)_. Consider two colors, **B** and **R**:

    B R R B B R R B 

If we add a **B** to the sequence, we a **B** at positions 1, 5 and 9 - a difference of 4. If we add an **R** to the sequence, we have an **R** at positions 3, 6 and 9 - a difference of 3. There is no way of coloring 1 through 9 without creating a three step progression of one color or another, so _W(2,3)=9_. 

Adding a color - _W(3,3)_ - causes the value to jump to 27; adding a length requirement to the arithmetic sequence - _W(2,4)_ - causes the value to increase to 35. 

Van der Waerden numbers are an open area of research, with exact values known for only a limited number of combinations. 

Your challenge today is to write a program that can calculate the Van der Waerden number for some small values.

# Input Description

You'll be given two integers per line indicating _c_ and _k_. Example:

    2 3

# Output Description

Your program should emit the Van der Waerden number _W(c,k)_ for that input. Example:

    W(2,3) = 9

# Challenge Input

    2 6
    4 3
    3 4

# Challenge Output

    W(2,6) = 1132
    W(4,3) = 76
    W(3,4) = 293
