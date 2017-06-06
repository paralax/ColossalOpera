# Title

Fencing In the Birds

# Difficulty

Intermediate

# Tags

math, geometry

# Description

Imagine that you're tasked with creating an aviary using a forest of randomly planted trees. But first you must designate the aviary to enclose the birds' habitat. To do so, imagine fencing it in using the trees as fenceposts to create a convex area, and you want to maximize how big that area can be. (If you allowed fo concave portions, you could allow in predators who could attack the birds and escape unseen.) 

A convex polygon is defined as a polygon where as you go around it, you always turn in the same direction. A square, for example, is a convex polygon, while a star is not (you turn left and right as you go around the perimeter either clockwise or counter-clockwise). 

Today's challenge is take a random scatter of points - those trees in the forest - and then to draw the largest convex polygon using a subset of those. The largest can be defined as covering the largest area or simply the largest perimeter - so long as it's a convex polygon. Just pick one approach and stick with it. 

This challenge was inspired in part by a recent breakthrough in the [Happy Ending Problem](https://www.quantamagazine.org/a-puzzle-of-clever-connections-nears-a-happy-end-20170530/?platform=hootsuite): 

_At a very general level, the happy ending problem is about finding ways to add sides to a polygon. Say you have five points. You know that this is enough to guarantee that you can construct a convex quadrilateral by connecting four of those points. From there, you want to increase the number of sides of that polygon — from four sides to five, six and beyond. As you do this, you need to keep track of the number of points you need to add in order to guarantee that you can make the desired shape._

For today's challenge, the aviary polygon can have as many sides as you wish so long as it's a convex polygon. 

# Input Description

You'll be given an array of points as _(x,y)_ coordinates, comma separated. These are Cartesian coordinates on a simple plane. Example:

	(1,1), (3,5), (3,2), (5,1)
	
# Output Description

Your program should emit the subset of points that maximize the aviary size of the convex polygon. From our example:

	(1,1), (3,5), (5,1)

This yields a simple triangle, the one with the largest perimeter of any of the triangles we could draw from these four points.

# Challenge Input

	(12, 17), (10, 4), (11, 12), (8, 2), (5, 11), (12, 11), (5, 15), (17, 13), (18, 14), (6, 12), (12, 16)
	
	(23, 8), (0, 21), (7, 17), (23, 5), (29, 17), (24, 21), (16, 14), (6, 28), (16, 10), (10, 27), (16, 19), (12, 28), (29, 6), (11, 2), (1, 18), (15, 8), (3, 6), (4, 12), (11, 17), (12, 21), (26, 0)
