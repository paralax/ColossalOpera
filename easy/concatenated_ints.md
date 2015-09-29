# Title 

Concatenated Integers

# Difficulty

Easy

# Description

Given a list of integers separated by a single space on standard input, print out the largest and smallest values that can be obtained by concatenating the integers together on their own line. This is from [Five programming problems every Software Engineer should be able to solve in less than 1 hour](https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour), problem 4. Leading 0s are not allowed (e.g. 01234 is not a valid entry). 

# Sample Input

You'll be given a handful of integers per line. Example:

	5 56 50

# Sample Output

You should emit the smallest and largest integer you can make, per line. Example:

	50556 56550

# Challenge Input

	79 82 34 83 69
	420 34 19 71 341
	17 32 91 7 46

# Challenge Output

	3469798283 8382796934
	193413442071 714203434119
	173246791 917463217

# Scala Solution

	// returns min, max
	def intConcat(s:String): (Long, Long) = {
		val l = s.split(" ").permutations.map(_.mkString.toLong).toList
		(l.sorted.head, l.sorted.reverse.head)
	}
