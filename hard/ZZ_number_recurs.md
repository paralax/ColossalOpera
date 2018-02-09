# Title

Which Number Recurs First

# Difficulty

Hard

# Tags

random numbers, big data, probabilistic data structures 

# Description

Working with very large data sets is an increasingly common activity in efforts such as web analytics and Internet advertising. Efficiently keeping track of values when you have 2^64 or greater values to keep track of. 

Today's challenge is to read a steady stream of distinct values and report on the first one that recurs. Your program should be able to run an arbitrary number of times with distinct, infinite sequences of input and yield the correct value. 

## Data source

I spent a good chunk of my morning trying to find a stream of random values for you to consume. I could not find one (e.g. a PRNG as a service) so I decided to use a local PRNG implementation. 

For this challenge, please use the following random number generator based on the Isaac design.

https://github.com/dkull/Isaac-CSPRNG/blob/master/Isaac.py

The above code expects a maximum integer passed to the `rand()` method, and for the purposes of this challenge set it to `sys.maxsize`. Then emit a steady stream of numbers and use your program to detect the first recurring value.

    import sys

    import Isaac
    i = Isaac.Isaac(noblock=False)
    while True:
        print(i.rand(sys.maxsize))

# Notes

This piece may prove a useful start: [PROBABILISTIC DATA STRUCTURES FOR WEB ANALYTICS AND DATA MINING](https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/). 
