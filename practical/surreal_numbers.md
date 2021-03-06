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

	class Surreal(var l:Set[Double], var r:Set[Double]) {
	    override def toString(): String = "{ " + l + " | " + r + " }"

	    // converts a real number to a surreal number
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

	    // operators
	    // more how to do this in scala:
	    // http://www.slideshare.net/joeygibson/operator-overloading-in-scala-2923973
	    // http://www.cut-the-knot.org/WhatIs/Infinity/SurrealNumbers.shtml

	    // negation
	    // https://gist.github.com/p3t0r/54679
	    def unary_- = new Surreal(this.r.map(_ * -1), this.l.map(_ * -1))

	    //def +(y:Surreal): Surreal = 
	    //    new Surreal((this.l + y) ++ (this + y.l), (this.r+y) ++ (this + y.r))

		def <=(y:Surreal): Boolean = 
			(((this.l.size == 0) || (this.l.max <= (y.l ++ y.r).min)) && 
			 ((y.r.size == 0) || (y.r.min > (this.l ++ this.r).max)))
		 
		def <(y:Surreal): Boolean = ((this <= y) && !(this == y))
	
		def >=(y:Surreal): Boolean = y <= this
	
		def >(y:Surreal): Boolean = ((this >= y) && !(this == y))
	
		def ==(y:Surreal): Boolean = ((this <= y) && (y <= this))
	}


	val s1 = new Surreal(1)
	val s2 = new Surreal(2)
	s1 <= s2
