# Title

A car renting problem

# Difficulty

Intermediate

# Description  

A carriage company is renting cars and there is a particular car for which the interest is the highest so the company decides to book the requests one year in advance. We represent a request with a tuple (x, y) where x is the first day of the renting and y is the last. **Your goal** is to come up with an optimum strategy where you serve the most number of requests. 

# Formal input and output  

The first line of the input will be *n* the number of requests. The following two lines will consist of n numbers for the starting day of the renting, followed by another n numbers for the last day of the renting corresponding. For all lines 0 &lt; ^x i &lt; ^y i &lt;= 365 inequality holds, where i=1, 2, ..., n. 

    10 
    1 12 5 12 13 40 30 22 70 19 
    23 10 10 29 25 66 35 33 100 65 

The output should be the maximum number of the feasibly requests and the list of these requests. One possible result may look like this: 

    4 
    (1,23) (30,35) (40,66) (70,100) 

But we can do better: 

    5 
    (5,10) (13,25) (30,35) (40,66) (70,100) 

Remember your goal is to find the scenario where you serve the most number of costumers.

# Notes

This problem was suggsted by /u/bessaai. If you have a challenge, please share it with /r/dailyprogrammer_ideas, there's a good chance we'll use it.
