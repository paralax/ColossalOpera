# Title

Playing the Stock Market

# Difficulty

Easy

# Description

Let's assume I'm playing the stock market - buy low, sell high. I'm a ay trader, so I want to get in and out of a stock before the day is done, and I want to time my trades so that I make the biggest gain possible. 

The market has a rule that won't let me buy and sell in a pair of ticks - I have to wait for at least one tick to go buy. And obviously I can't buy in the future and sell in the past. 

So, given a list of stock price ticks for the day, can you tell me what trades I should make to maximize my gain within the constraints of the market? Remember - buy low, sell high. 

# Input Description

You'll be given a list of stock prices as a 2 decimal float (dollars and cents), listed in chronological order. Example:

    19.35 19.30 18.88 18.93 18.95 19.03 19.00 18.97 18.97 18.98

# Output Description

Your program should emit the two trades in chronological order - what you think I should buy at and sell at. Example:

    18.88 19.03

# Challenge Input

    8.10 8.03 8.02 8.08 8.14 8.10 8.31 8.28 8.35 8.34 8.39 8.45 8.38 8.38 8.32 8.36 8.28 8.28 8.38 8.48 8.49 8.54 8.73 8.72 8.76 8.74 8.87 8.82 8.81 8.82 8.85 8.85 8.86 8.63 8.70 8.68 8.72 8.77 8.69 8.65 8.70 8.98 8.98 8.87 8.71 9.17 9.34 9.28 8.98 9.02 9.16 9.15 9.07 9.14 9.13 9.10 9.16 9.06 9.10 9.15 9.11 8.72 8.86 8.83 8.70 8.69 8.73 8.73 8.67 8.70 8.69 8.81 8.82 8.83 8.91 8.80 8.97 8.86 8.81 8.87 8.82 8.78 8.82 8.77 8.54 8.32 8.33 8.32 8.51 8.53 8.52 8.41 8.55 8.31 8.38 8.34 8.34 8.19 8.17 8.16

# Challenge Output

# Python Quote Generator

    import random

    def stockprices(init, sofar=[]): 
        if len(sofar) == 100: return sofar
        else:
            sofar.append(init + (random.paretovariate(init)-random.paretovariate(init))*0.5)
            return stockprices(sofar[-1], sofar)

    print ' '.join(map(lambda x: '%.2f' % x, stockprices(8, [])))

# Scala Solution
