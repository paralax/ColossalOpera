**Title** Word Wheel

**Difficulty** Intermediate

**Description**

A word wheel is a puzzle where there's a series of letters on the outside of a circle and one in the middle. You then have to find as many words as possible that contain the letter in the middle and two or more of the letters on the outside.

For this challenge you'll be asked to solve word wheels. 

**Sample Input**

You'll be given a word wheel as a small piece of ASCII art. Because wheels in ASCII are very tough, instead you'll be given three lines. The middle line will be the center of the wheel and the first and third lines will be the outside of the wheel. For your dictionary use /usr/share/dict/words or the classic enable1.txt file: http://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt

	e f t
	  i
	p   d

**Sample Output**

Your program should emit all words of the maximum length. For the above wheel we get:

	tepid
	fetid

**Challenge Input**

	t a f e
	   m
	 b i s

**Challenge Output**

	teaism
	semita
	samite

**Credit** 

Many thanks to Ben Everard for the idea!
