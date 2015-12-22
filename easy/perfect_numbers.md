# Title 

Perfect Numbers

# Difficulty

Easy

# Tags

divisors, number theory, math, integer sequence

# Description

In number theory, a [perfect number](http://en.wikipedia.org/wiki/Perfect_number) is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128. 

In this challenge you'll be asked to calculate an arbitrary number of perfect numbers. 

# Input Description

You'll be given a single integer, *N*, which tells you how many perfect numbers to emit. Example:

	4

# Output Description

Your program should emit a list of perfect numbers up to that point. For our example:

	6 28 496 8128

# Challenge Input

	10

# Challenge Output

	6 28 496 8128 33550336 8589869056 137438691328 2305843008139952128 2658455991569831744654692615953842176 191561942608236107294793378084303638130997321548169216

# Scala Solution

a naive solution that doesn't use the Euclid-Euler theorem

	def factors(n:Int): List[Int] = (2 to n/2).filter(x => n%x == 0).toList

	def perfect(n:Int): Boolean = n == factors(n).sum + 1

	(1 to 10000).filter(perfect(_))

getting closer to using Euclid-Euler

	def isprime(n:Int) : Boolean = {
		def check(i:Int) : Boolean = (i > n/2) || ((n % i != 0) && (check (i+1)))
		check(2)
	}

	def perfect(n:Int): Long = (scala.math.pow(2, (n-1))*(scala.math.pow(2, n)-1)).toLong

	(2 to 50000).filter(isprime(_)).map(perfect(_)).distinct
	
