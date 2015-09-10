# Title

Calkin-Wilf Tree

# Difficulty

Intermediate

# Description

In number theory, the Calkin–Wilf tree is a tree in which the vertices correspond 1-for-1 to the positive rational numbers. The tree is rooted at the number 1, and any rational number expressed in simplest terms as the fraction a/b has as its two children the numbers a/(a + b) and (a + b)/b. Every positive rational number appears exactly once in the tree.

The children of any vertex in the Calkin–Wilf tree may be computed by inverting the formula for the parents of a vertex. Each vertex a/b has one child whose value is less than 1, a/(a + b), because this is the only value less than 1 whose parent formula leads back to a/b. Similarly, each vertex a/b has one child whose value is greater than 1, (a + b)/b.

# Input Description

You'll be given an integer on a line, *n*. This is the depth of the tree to which you should generate (with the root as depth 1). For example:

    3

# Output Description

Your program should emit the sequence of rational numbers at that depth. For example:

    3 -> 1/3, 3/2, 2/3, 3/1

# Challenge Input

    10
    
# Challenge Output

TBD

https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree

# Scala Solution

    class Rational(numerator: Int, denominator: Int) {

      require(denominator != 0)

      private val gcd = greatestCommonDivisor(numerator.abs,
        denominator.abs)
      val n = numerator / gcd
      val d = denominator / gcd

      def this(n: Int) = this(n, 1)

      private def greatestCommonDivisor(a: Int, b: Int): Int =
      if (b == 0) a else greatestCommonDivisor(b, a % b)

      def + (that: Rational): Rational =
      new Rational(n * that.d + d * that.n, d * that.d)

      def - (that: Rational): Rational =
      new Rational(n * that.d - d * that.n, d * that.d)

      def * (that: Rational): Rational =
      new Rational(n * that.n, d * that.d)

      def / (that: Rational): Rational =
      new Rational(n * that.d, d * that.n)

      override def toString = n + "/" + d
    }


    def leaf(r:Rational): (Rational, Rational) = (new Rational(r.n, r.n+r.d),  new Rational(r.n+r.d,r.d))
    def leafToList(rr:(Rational,Rational)): List[Rational] = List(rr._1, rr._2)

    def calkin_wilf(n:Int): List[Rational] = {
        val root = new Rational(1,1)
        def loop(r:Rational): List[Rational] = {
            leafToList(leaf(r)).flatMap(x => leafToList(leaf(x)))
        }
        var res = loop(root)
        for (_ <- (2 to n-1)) {
            res = res.flatMap(loop)
        }
        res
    }
