# Title

New York Street Sweeper Paths

# Difficulty

Hard

http://en.wikipedia.org/wiki/Route_inspection_problem

http://www.oocities.org/harry_robinson_testing/graph_theory.htm

# Description

In graph theory, various walks and cycles occupy a number of theorems, lemmas, and papers. They have practical value, it turns out, in a wide variety of applications: computer networking and street sweepers among them. 

For this challenge you're the commissioner of NYC street sweeping. You have to keep costs down and keep the streets clean, so you'll minimize the number of streets swept twice while respecting traffic directionality. The goal of this challenge is to visit all edges at least one while minimizing the number of streets swept to the bare minimum. 

Can you find a route to give your drivers? 

# Input Description

Your program will be given two integers on one line which tell you hot tall and wide the street map is. On the next line will be a single uppercase letter telling you where to begin. Then the ASCII map will begin using the dimensions you were given. Your tour should end the day at the starting point.

You'll be given an ASCII art graph. Intersections will be named as uppercase letters A-Z. Streets will connect them. The streets may be bi-directional (- or |) or one-way (one of ^ for up only, v for down only, < for left only, and > for right only) and you may not violate the rules of the road as the commissioner. 

# Output Description

Your program should emit the intersections visited in order and the number of street segments you swept. 

# Challenge Input

	3 3
	F 
	A - B - C
	|   |   v
	D > E - F
	^   v   v
	G - H < I

# Challenge Output

TBD