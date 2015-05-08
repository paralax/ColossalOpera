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


	class Surreal(l:Set[Double], r:Set[Double]) {
		def +(y:Surreal) = 
			new Surreal((this.l + y) ++ (this + y.l), (this.r+y) ++ (this + y.r))
	
		override def toString(): String = "{ " + l + " | " + r + " }"
	}

	def dali(x:Int): Surreal = {
		x match {
			case 0 => new Surreal(Set(), Set())
			case y if y > 0 => dali(y-1)
			case y if y < 0 => dali(y+1)
		}
	}
