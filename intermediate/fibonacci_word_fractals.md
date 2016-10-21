# Title
 
Fibonacci Word Fractals

# Difficulty

Intermediate

# Tags

ASCII art, fibonacci, fractal

# Description

The infinite Fibonacci word is a specific infinite sequence in a two-letter alphabet. Similar to how the Fibonacci sequence is built, we start with the first two entries (f_1 = 1, f_2 = 0) and build successive parts of the word by combining the previous two (f_n = f_(n-1)f_(n-2)), so f_3 is 01, f_4 is 010 and so on. 

You can take this sequence and construct an interesting fractal using these steps:

- Take the n^(th) digit of the Fibonacci word
- Draw a segment forward
- If the digit is 0 then
  - turn left if *n* is odd
  - turn right if *n* is even

If this is a bit confusing, see [this accessible paper by Alexis Monnerot-Dumaine](https://hal.archives-ouvertes.fr/hal-00367972/document) for more information. 

When you do this, you wind up with curves that look like this:

	######
	#    #
	#    ###

Today's challenge is to implement code that can draw the fractal using ASCII art (or graphics if you're so inclined, for example using JavaScript or Matplotlib). You'll no doubt have to scale your artwork given how big you make it. 
