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


	class Surreal(var l:Set[Double], var r:Set[Double]) {
	    override def toString(): String = "{ " + l + " | " + r + " }"
	
		def this(x:Double) { 
			this(Set(0.0), Set(0.0))
			(x%1.0) match {
		        case 0.0 => x match {
		                        case 0 => this(Set(), Set())
		                        case y if y > 0 => this(Set(y-1), Set())
		                        case y if y < 0 => this(Set(), Set(y+1))
		                    }
		        case _   => x match { // this needs some attention, wrong calculations here
								case y if y > 0 => this(Set(y/2.0), Set(y+(y/2.0)))
								case y if y < 0 => this(Set(y+(y/2.0)), Set(y/2.0))
							}	
		    }
		}
	
		def apply(l:Set[Double], r:Set[Double]) = {
			this.l = l
			this.r = r
		}

	    //def +(y:Surreal): Surreal = 
	    //    new Surreal((this.l + y) ++ (this + y.l), (this.r+y) ++ (this + y.r))

	}
