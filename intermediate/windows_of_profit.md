# Title

Windows of Profit

# Difficulty

Intermediate

# Tags

Kadane's algorithm, Bae and Takoaka's algorithm, subarray sum

# Description

I like to play the stock market, and recent volatility has got me thinking: on which days over the past ten days should I have played the market? Granted, you can't trade on history, but maybe I can learn something from this.

To do this, I'd like to know which contiguous days - subarrays - I should group together for my losses and profits to maximize my sum. Subarrays may be of length 1 or more. 

I need your help to make some money.

# Input Description

You'll be given two lines per input, the first is an array of daily price changes including postive and negative integers, and the second is the number *k* of subarrays to calculate the *k* maximal sums. Example:

    -10 -9 -2 7 -4 6 4 -7 -6 -4
    3

# Output Description

Your program should emit the values of top *k* maximimal subarray sums. From the above example:

    13 11 10 

# Challenge Input

    -7 2 -8 -5 3 8 -2 6 9 1
    4
    ----
    -1 3 -3 -8 4 -9 1 -1 6 2
    4

# Challenge Output

    25 24 22 21
    ----
    8 8 7 6
