# Title

Drainage Ditches

# Difficulty

Hard

# Tags

computational geometry

# Description

Every time it rains on Farmer John's fields, a pond forms over Bessie's favorite clover patch. This means that the clover is covered by water for awhile and takes quite a long time to regrow. Thus, Farmer John has built a set of drainage ditches so that Bessie's clover patch is never covered in water. Instead, the water is drained to a nearby stream. Being an ace engineer, Farmer John has also installed regulators at the beginning of each ditch, so he can control at what rate water flows into that ditch. 

Farmer John knows not only how many gallons of water each ditch can transport per minute but also the exact layout of the ditches, which feed out of the pond and into each other and stream in a potentially complex network. 

Given all this information, determine the maximum rate at which water can be transported out of the pond and into the stream. For any given ditch, water flows in only one direction, but there might be a way that water can flow in a circle. 

# Input Description

You'll be given two integers on the first line, *N* and *M*. *N* tells you how many intersections for *M* number of ditches.  The next *N* lines will inform you of the flow points (from *x* to *y*) and the capacity. 

# Output Description

Your program should emit the maxiumum flow rate as the pond drains. 

# Challenge Input

    5 4
    1 2 40
    1 4 20
    2 4 20
    2 3 30
    3 4 10

# Challenge Output

    50

This challenge was found via [this university programming challenge website](http://poj.org/problem?id=1273).