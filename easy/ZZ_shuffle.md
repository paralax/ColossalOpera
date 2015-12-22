# Title 

[2015-07-20] Challenge #224 [Easy] Shuffling a List

# Difficulty

Easy

# Tags

algorithm, shuffle, Fisher-Yates, Faro

# Description

We've had our fair share of sorting algorithms, now let's do a *shuffling* challenge. In this challenge, your challenge is to take a list of inputs and change around the order in random ways. Think about shuffling cards - can your program shuffle cards?

# Input Description

You'll be given a list of values - integers, letters, words - in one order. The input list will be space separated. Example:

	1 2 3 4 5 6 7 8 

# Output Description

Your program should emit the values in any non-sorted order; sequential runs of the program or function should yield different outputs. You should maximize the disorder if you can. From our example:

	7 5 4 3 1 8 2 6

# Challenge Input

	apple blackberry cherry dragonfruit grapefruit kumquat mango nectarine persimmon raspberry raspberry
	a e i o u

# Challenge Output 

Examples only, this is all about shuffling

	raspberry blackberry nectarine kumquat grapefruit cherry raspberry apple mango persimmon dragonfruit
	e a i o u

# Bonus

Check out the Faro shuffle and the Fisher Yates shuffles, which are algorithms for specific shuffles. Shuffling has some interesting mathematical properties. 

# Scala Solution

	def fischer_yates_shuffle(l:List[Int]): List[Int] = {	
		def loop(l:List[Int], n:Int): List[Int] = {
			(l.length == n) match {
				case true   => l
				case false  => val i = (scala.math.random*l.length).toInt
	  						   l.slice(0, n) ++ List(l(i)) ++ l.slice(n+1,i) ++ List(l(n)) ++ l.slice(i+1,l.length)
			}
		}
		loop(l, 0)
	}

	def faro_shuffle(l:List[Int], steps:Int): List[Int] = {
		def loop(l:List[Int], n:Int): List[Int] = {
			(n == 0) match {
				case true  =>   l
				case false =>   val (a,b) = (l.slice(0, l.length/2), l.slice(l.length/2, l.length))
								if (a.length != b.length) {
									loop(a.zip(b).flatMap(x => List(x._1, x._2)) ++ List(b.last), n-1)
								} else {
									loop(a.zip(b).flatMap(x => List(x._1, x._2)), n-1)
								}
			}
		}
		loop(l, steps)
	}
