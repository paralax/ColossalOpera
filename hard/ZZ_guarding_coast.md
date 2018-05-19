# Title

Guarding the Coast

# Difficulty

Hard

# Tags

geometry, computational geometry

# Description

Imagine you're in charge of the coast guard for your island nation, but you're on a budget. You have to minimize how many boats, helicopters and crew members to adequately cover the coast. Each group is responsible for a square area of coastline. 

It turns out this has a mathematical relationship to some interesting mathematics. In fractal geometry, the [Minkowski–Bouligand Dimension](https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension), or box counting dimension, is a means of counting the fractal geometry of a set *S* in Euclidian space R^n. Less abstractly, imagine the set *S* laid out in an evenly space grid. The box counting dimension would be the minimum number of square tiles required to cover the set.

More realistically, when doing this counting you'll wind up with some partial tiles and have to overlap, and that's OK - overlapping boxes are fine, gaps in coastal coverage are not. What you want to do is to minimize the number of tiles overall. It's easy over estimate, it's another to minimize. 

# Input Description

You'll be given two things: a tile size N representing the side of the square, and an ASCII art map showing you the coastline to cover. 

Example:

	2
	
	*****
	*   *
	*   *
	*   *
	*****

# Output Description

Your program should emit the minimum number of tiles of that size needed to cover the boundary. 

From the above example:

	8
	
# Challenge Input

	4
                          
						 **
					   *   **
					  *     *
					 **      *
					*        *
				   **         *
				  *            *
				 *            *
				  **        **
				    *      *
				  **        ***
				 *             *
				*               *
			  **                *
			 *                   **
			**                     *
		  **                        *
		 *                        **
		  *                     **
		   *                 ***
		    **              *
	       *                 *
    	 **					  **
		*                 ****
		 **         ******           
		   *********   
