# Title

Snake in a box

# Difficulty

Hard

# Tags

graph theory

# Description

The snake-in-the-box problem in graph theory and computer science deals with finding a certain kind of path along the edges of a hypercube. This path starts at one corner and travels along the edges to as many corners as it can reach. After it gets to a new corner, the previous corner and all of its neighbors must be marked as unusable. The path should never travel to a corner after it has been marked unusable.

Imagine a 3-dimensional cube with corners labeled with three digit numbers of the *x,y,z* coordinates: 000, 001, 011, 010, 100, 101, 111, 110. The longest tour of this cube, given the rules above, follows the path 000 -> 001 -> 011 -> 111 -> 110 for a length of 4. 

As you may imagine, as the dimensionality of the hypercube grows the complexity also grows. For dimensions above 9 there is no concrete answer, only longest lengths found so far. 

# Input Description

You'll be given a single digit *n* per line indicating the dimensionality of the cube on which to operate. Example:

    3

# Output Description

Your program should emit the length of the longest edge traversal path it can find following the constraints above. You should also emit the corners toured - consider using the labeling system from above. Example:

    4 = 000 -> 001 -> 011 -> 111 -> 110

# Challenge Input

    4
    6
    8

The 8D hypercube will really stress the efficiency of your algorithm. 
