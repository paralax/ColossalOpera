# Title

[2017-08-09] Challenge #326 [Intermediate] Scrabble in Reverse

# Difficulty

Intermediate

# Tags

scrabble

# Description

Many of us have played Scrabble, the game where you lay down tiles of letters on a board to form interlocking valid English language words. Players get points depending on the tiles they play and the bonus squares they use per word. 

Now, can you reverse a Scrabble game? That is, given a board can you infer what words were played and in what order?

Given some basic rules of Scrabble:

- The first word should be as centered as possible on the middle square (horizontal and vertical centering)
- Each play must build off the previous word
- Each play must yield valid English language words (one or more)
- Words may be extended (e.g. "can" can become "cans", either by adding a single letter or by playing a new word that intersects to form a second valid word)

For your dictionary, use any standard English language dictionary (or [enable1.txt](https://github.com/dolph/dictionary/blob/master/enable1.txt)).

# Example Input

You'll be given two integers on a line telling you how many rows and columns to read, then a board (with those dimensions) with words filled out, with blank spaces using a period `.`. Example:

	7 8
	...cite
	.tilt..
	...e...
	.planes
	...n...
	.......
	.......

# Example Output

Your program should emit one or more words, in the order in which they were played (first to last). Example:

	planes
	clean
	cite
	tilt

An alternative could be:

	planes
	clean
	tilt
	cite

# Challenge Input


	9 10
	.........
	.........
	.ferries.
	.l.....t.
	.o..an.a.
	.e...e.f.
	.short.f.
	.......e.
	..called.

# Challenge Output

	an
	net
	short
	floes
	ferries
	staffed
	called
