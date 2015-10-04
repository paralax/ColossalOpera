# Title

Finding the McSpot

# Difficulty

Hard

# Description

The idea for this challenge is a simplified version of finding the location in the Continental United States which is the furthest distance from any McDonald's. Given a known boundary, and a set of 'locations' determine a the spot which is the furthest from any location.

# Input

Your program should take the bounding rectangle defined by the two integers *n* and *m*, defining its size, and *i*, the count of location points. The map points will be given as "(x,y)" pairs of integers. All points were generated at random with no particular weighting or bias.

For this challenge you'll probably want to study up on Voronoi diagrams. 

# Output Description 

Find the coordinate (x,y) furthest from any of the given location points. The (x,y) coordinate should be to the 6th decimal place. Why 6? Because latitude and longitude taken to 6 decimal places is accurate to about 1 meter.

# Challenge Input

    500 500 20
    (104, 209)
    (16, 234)
    (76, 63)
    (44, 472)
    (489, 43)
    (304, 139)
    (72, 164)
    (414, 470)
    (147, 46)
    (464, 150)
    (371, 229)
    (414, 198)
    (316, 172)
    (132, 248)
    (477, 345)
    (118, 473)
    (19, 308)
    (42, 409)
    (45, 141)
    (456, 210)

# Bonus Input

Here's a gist file with even more points. https://gist.github.com/paralax/f1f0fb5af50d5c9c7b6e

# Credit

Many thanks to Redditor /u/strongpassword for this submission. 
https://github.com/gavinr/usa-mcdonalds-locations

# Notes

Have a cool challenge idea? Post it to /r/DailyProgrammer_Ideas!