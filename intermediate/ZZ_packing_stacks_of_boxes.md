# Title

Packing Stacks of Boxes

# Tags

sorting, recursion

# Difficulty

Intermediate

# Description

You run a moving truck business, and you can pack the most in your truck when you have stacks of equal size - no slack space. So, you're an enterprising person, and you want to write some code to help you along. 

# Input Description

You'll be given two numbers per line. The first number is the number of stacks of boxes to yield. The second is a list of boxes, one integer per size, to pack. 

Example:

	2 343123321

That says "make two stacks of boxes with sizes 3, 4, 3, 1 etc". 

# Output Description

Your program should emit the stack of boxes as a series of integers, one stack per line. From the above example:

	331
	322
	34

If you can't make equal sized stacks, your program should emit nothing. 

# Challenge Input

	3 912743471352
	3 42137586
	9 2 
	4 064876318535318

# Challenge Output

	9124
	7342
	7135

	426
	138
	75

	(nothing)
	
	0665
	4733
	8315
	881

# Scala Solution

	import scala.annotation.tailrec

	def elemsEqual(L:List[Int]): Boolean = 
		L.distinct.length == 1 
	
	def pack(n:Int, boxes:List[Int]): List[List[Int]] = {
		val g = boxes.permutations	
		@tailrec def loop(g:Iterator[List[Int]]): List[List[Int]]= {
			val s = g.next.grouped(n).toList
			(elemsEqual(s.map(_.sum)) && (s.length == n)) match {
				case true  => s
				case false => loop(g)
			}
		}
		try {loop(g)}
		catch {
			case _ => List(List[Int]())
		} 
	}

	val boxes = args(2).toCharArray.map(_.toString.toInt).toList
	println(pack(args(1)toInt, boxes).map(_.mkString).mkString("\n"))
