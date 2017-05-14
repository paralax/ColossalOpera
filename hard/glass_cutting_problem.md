# Title

Glass Cutting Optimization

# Difficulty

Hard

# Tags

geometry

# Description

The Guillotine problem is important in glass machining. Glass sheets are scored along horizontal and vertical lines and then broken along these lines to obtain smaller panels.

The guillotine problem is a problem in combinatorial geometry and in printing. It is the question of how to get the maximum number of sheets of one rectangular size out of a larger sheet, only orthogonal cuts that bisect one component of the sheet are allowed, as on a paper cutting guillotine.

Today's challenge is to implement an algorithm that can cut the glass and minimize waste. 

# Input Description

You'll be given inputs over two lines. The first line tells you how big the sheet of glass is. The second line tells you pairs of numbers to tell you what size of sheets to make. Example:

	20 4
	4 15 4 5

Meaning glass pieces sized 6 5x7, 9 4x6, 2 2x3.5, and 5 3x5. 

# Output Description

Your program should emit the sequence of cuts to make using x,y coordinates and stating the start and end positions that yield the desired pieces and minimizes waste. Assume 0,0 is the upper left corner. Example:

	 15 0 15 4

Meaning start cutting at 15,0 and cut to 15,4. 

# Challenge Input

	4 8
	1 3 2 3 3 3 1 5 2 4
	22 24
	5 7 5 7 5 7 5 7 5 7 5 7 4 6 4 6 4 6 4 6 4 6 4 6 4 6 4 6 4 6 2 3.5 2 3.5 3 5 3 5 3 5 3 5 3 5
	20 24
	4 15 4 5 12 5 17 4 5 6 11 6 13 3 10 3 10 6 5 5 4 5 4 5 4 9 5 2 4 2 
