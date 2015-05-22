# Title

Change Ringing

http://en.wikipedia.org/wiki/Change_ringing

# Difficulty

Intermediate

# Description

Change ringing is the art of ringing a set of tuned bells in a series of mathematical patterns called "changes". Change ringing differs from many other forms of campanology (such as carillon ringing) in that no attempt is made to produce a conventional melody. Developed in the 17th century, change ringing remains popular in England.

Permutations of the bells are done a pair at a time. Each row of bells is then rung once per row in that order before the next permutation and ringing. An example of this method is this set of rows, where 1 pair of neighbors is swapped for each permutation. This method yields the following pattern: 

1,2,3,4,5,6	
1,3,2,4,5,6	
1,3,2,5,4,6	
1,3,5,2,4,6	
3,1,5,2,4,6	
...

For some people, the ultimate goal of this system is to ring all the permutations, to ring a tower's bells in every possible order without repeating — what is called an "extent" (or sometimes, formerly, a "full peal"). This pattern continues until the original ordering is returned. There are *N!* permutations.

# Input Description

For this challenge you'll be given a single integer, *N*, which is the number of bells to organize.

# Output Description

Your program should emit the complete list of steps to take in the permutation, the "full peal". 

# Challenge Input

	6

# Challenge Output

