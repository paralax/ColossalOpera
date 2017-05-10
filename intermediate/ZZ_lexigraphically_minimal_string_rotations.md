# Title

[2017-05-10] Challenge #314 [Intermediate] Comparing Rotated Words 

# Difficulty

Intermediate

# Tags

words, circular

# Description

We've explored the concept of string rotations before as [garland words](https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/?ref=search_posts). Mathematically we can define them as a string *s* = *uv* is said to be a rotation of *t* if *t* = *vu*. For example, the string 0011001 is a rotation of 0100110, where *u* = 00110 and *v* = 01.

Today we're interested in *lexicographically minimal string rotation* or lexicographically least circular substring, the problem of finding the rotation of a string possessing the lowest lexicographical order of all such rotations. Finding the lexicographically minimal rotation is useful as a way of normalizing strings. 

# Input Description

You'll be given strings, one per line. Example:

	aabbccddbbaabb

# Output Description

Your program should solve the lexicographically minimal string rotation and produce the size of the substring to move and the resulting string. Example:

	10 aabbaabbccddbb

Which is, in Python parlance, `"aabbccddbbaabb"[10:] + "aabbccddbbaabb"[:10]`. 

# Challenge Input

	onion
	bbaaccaadd
	alfalfa
	weugweougewoiheew
	pneumonoultramicroscopicsilicovolcanoconiosis

# Challenge Output

	2 ionon
	2 aaccaaddbb
	6 aalfalf
	14 eewweugweougewoih
	12 amicroscopicsilicovolcanoconiosispneumonoultr
