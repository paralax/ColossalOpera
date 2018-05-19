# Title

Friedman numbers

# Difficulty

Intermediate

# Tags

math, puzzle

# Description

A Friedman number is an integer, which in a given base, is the result of an expression using all its own digits in combination with any of the four basic arithmetic operators (+, -, *, /), additive inverses, parentheses, and exponentiation. For example, 347 is a Friedman number, since 347 = 7^3 + 4. Parentheses can be used in the expressions, but only to override the default operator precedence, for example, in 1024 = (4 - 2)10. Allowing parentheses without operators would result in trivial Friedman numbers such as 24 = (24). Leading zeros cannot be used, since that would also result in trivial Friedman numbers, such as 001729 = 1700 + 29.

Two special cases of Friedman numbers worth noting: A **nice or "orderly" Friedman number** is a Friedman number where the digits in the expression can be arranged to be in the same order as in the number itself. For example, we can arrange 127 = 2^7 - 1 as 127 = -1 + 2^7. **Vampire numbers** are a type of Friedman numbers where the only operation is a multiplication of two numbers with the same number of digits, for example 1260 = 21 * 60.

# Input Description

You'll be given a number, which may or may not be a Friedman number, one per line. Examples:

    127
    2502
    576

# Output Description

You'll be asked to output the formula that results in the value according to Friedman number rules, or a statement that it is not:

    127 = 2^7+1
    2502 = 50^2+2
    576 NOT VALID

# Challenge Input

    343
    1285
    8147
    123456789

# Challenge Output

    343 = (3+4)^3
    1285 = (1+2^8)+5
    8147 NOT VALID
    123456789 = ((86 + 2 * 7)5 - 91) / 34

# Notes 

The [August 2000 Math Magic](http://www2.stetson.edu/~efriedma/mathmagic/0800.html) problem was around Friedman numbers, here are many of them decomposed. 