# Title

Create a Simple Stochastic Computing Machine

# Difficulty

Hard

# Tags

stochastic computing, analog computing, logic

# Description

[Stochastic computing](https://en.wikipedia.org/wiki/Stochastic_computing), first introduced by the noted scientist John von Neumann in 1953, is a collection of techniques that represent continuous values (for example probabilities between 0 and 1) using streams of random bits. The bits in the stream represent the probabilities. Complex computations can then be computed over these stream by applying simple bit-wise operations.

For example, given two probabilities _p_ and _q_, using 8 bits, to represent the probabilities 0.5 and 0.25:

    10011010
    01010000

To calculate _p_ x _q_ we apply the logical AND over the bitstream:

    00010000

Yielding 1/8, or 12.5%, the correct value. For an 8-bit stream, this is the smallest unit of precision we can calculate. To increase precision we must increase the size of the bitstream. 

This approach has a few benefits in a noisy environment, most importantly a tolerance for loss (for example in transmission) and better fidelity over various bit lengths. However, precision comparable to a standard binary computer requires a significant amount of data - 500 bits in a stochastic computer to get to 32-bit precision in a binary computer. 

Your challenge today is to build a basic stochastic computer for probabilistic inputs, supporting the four major arithmetic operations:

* Addition
* Subtraction
* Multiplication
* Division

Be sure to measure the precision and fidelity of your machine, I encourage you to explore the tradeoffs between space and accuracy. 

# Notes

* [Survey of Stochastic Computing](https://homes.cs.washington.edu/~armin/ACM_TECS_2013.pdf) - journal paper from ACM on stochastic computing that explains it better than I did above.
* [Stochastic Computing Systems](https://pages.cpsc.ucalgary.ca/~gaines/reports/COMP/SCS69/SCS69.pdf) - book chapter on stochastic computers
