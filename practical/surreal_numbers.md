# Title

Project: Surreal Numbers

# Description

http://en.wikipedia.org/wiki/Surreal_number
http://scienceblogs.com/goodmath/2006/08/21/arithmetic-with-surreal-number/
http://senseis.xmp.net/?SurrealNumbers

If x = { XL | XR } and y = { YL | YR } are surreal numbers, then

x + y = {XL + y ∪ x + YL | XR+y ∪ x + YR} where

* if X is a set of surreal numbers, and y is a surreal number, then X+y = {x+y|x ∈ X}.


# Scala Implementation

cribbing from https://github.com/codeinthehole/python-surreal/blob/master/src/surreal.py


	class Surreal(l:Set[A], r:Set[A]) {
		def this(l:Int, r:Int) {this()}
		def this(l:Double, r:Int) {this()}
		def this(l:Int, r:Double) {this()}
		def this(l:Double, r:Double) {this()}
		
		def valid(l, r): Boolean = true
	
		def +(y:Surreal) = 
			new Surreal((this.l + y) ++ (this + y.l), (this.r+y) ++ (this + y.r))

		override def toString(): String = "{ " + l + " | " + r + " }"
	}

	def dali(x:Double): Surreal = {
		(x%1.0) match {
			case 0.0 => x match {
							case 0 => new Surreal(Set(), Set())
							case y if y > 0 => new Surreal(Set(y-1), Set())
							case y if y < 0 => new Surreal(Set(), Set(y+1))
						}
			case _   => new Surreal(Set(x/2.0), Set(x*2.0))
		}
	}
