# Title

Subfactorials - Another Twist on Factorials

# Difficulty

Easy

# Tags

math, number theory, cobinatorics

# Description

Most everyone who programs is familiar with the factorial - _n!_ - of a number, the product of the series from _n_ to _1_. One interesting aspect of the factorial operation is that it's also the number of permutations of a set of _n_ objects. 

Today we'll look at the _subfactorial_, defined as the *derangement* of a set of _n_ objects, or a permutation of the elements of a set, such that no element appears in its original position. We denote it as _!n_. 

Some basic definitions:

!1 -> 0 because you always have {1}, meaning 1 is always in it's position.
!2 -> 1 because you have {2,1}.
!3 -> 2 because you have {2,3,1} and {3,1,2}. 

And so forth. 

Today's challenge is to write a subfactorial program. Given an input _n_, can your program calculate the correct value for _n_?

# Input Description

You'll be given inputs as one integer per line. Example:

    5

# Output Description

Your program should yield the subfactorial result. From our example:

    9

# Challenge Input

    6
    9
    14

# Challenge Output

    !6 -> 265
    !9 -> 133496
    !14 -> 32071101049

# Bonus

Try and do this as code golf - the shortest code you can come up with.

# Double Bonus

Enterprise edition - the most heavy, format, ceremonial code you can come up with in the enterprise style.
