# Title

Sturdy Brick Walls

# Difficulty

Intermediate

# Description

A brick wall is a rectangle made of horizontal 1-by-n bricks stacked into rows. A wall is sturdy if no two vertical edges of bricks appear in the same line. Here's an example of a sturdy wall:

	[___][___]
	_][___][__
	[___][___]

And here's an example of a wall with a fault (it is not sturdy):

	[______][______]   
	[__][____][__][]   
	[][______][____]   
	[____][______][]   

In this challenge your task is to create walls at least three bricks high that are sturdy.

# Input Description

You'll be given a list of integers that correspond to brick widths. Draw your bricks like this (e.g. the number tells you how many underscores to draw):

	1: [_]
	2: [__]
	3: [___]
	4: [____]
	...

# Output Description

Your program should emit a sturdy brick wall as ASCII art. If you have more than one possible solution, draw one or more.

# Challenge Input

	1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
	1, 2, 3, 4, 5, 6, 7, 8, 9
	1, 1, 2, 2, 3, 3, 3, 3

# Challenge Output

	[][__][__]
	[__][__][]
	[][__][__]
	[__][__][]
	[][__][__]

	[][______________]
	[__][____________]
	[________________]
	[____][__________]
	[______][________]

	[][__][____]
	[__][____][]
	[____][____]
