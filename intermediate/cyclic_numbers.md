# Title

Constructing Cyclic Numbers

# Difficulty

Intermediate

# Description

https://en.wikipedia.org/wiki/Cyclic_number 

A cyclic number is an integer in which cyclic permutations of the digits are successive multiples of the number. 

Cyclic numbers can be constructed using the following steps: 

1. Let b be the number base (10 for decimal)
1. Let p be a prime that does not divide b.
1. Let t = 0.
1. Let r = 1.
1. Let n = 0.
1. loop:

    1. Let t = t + 1
    1. Let x = r * b
    1. Let d = int(x / p)
    1. Let r = x mod p
    1. Let n = n * b + d
    1. If r != 1 then repeat the loop.

1. if t = p − 1 then n is a cyclic number.

Your challenge today is a bit different than a typical challenge. Instead of creating or hunting for an algorith, your challenge is to *implement* the above algorithm and create some cyclic numbers. 
