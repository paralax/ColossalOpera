# Title

Calkin-Wilf Tree

# Difficulty

Intermediate

# Tags

math, rational numbers, rational sequence

# Description

In number theory, the [Calkin–Wilf tree](https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree)  is a tree in which the vertices correspond 1-for-1 to the positive rational numbers. The tree is rooted at the number 1, and any rational number expressed in simplest terms as the fraction a/b has as its two children the numbers a/(a + b) and (a + b)/b. Every positive rational number appears exactly once in the tree.

The children of any vertex in the Calkin–Wilf tree may be computed by inverting the formula for the parents of a vertex. Each vertex a/b has one child whose value is less than 1, a/(a + b), because this is the only value less than 1 whose parent formula leads back to a/b. Similarly, each vertex a/b has one child whose value is greater than 1, (a + b)/b.

# Input Description

You'll be given an integer on a line, *n*. This is the depth of the tree to which you should generate (with the root as depth 1). For example:

    3

# Output Description

Your program should emit the sequence of rational numbers at that depth. For example:

    3 -> 1/3, 3/2, 2/3, 3/1

# Challenge Input

    5
    
# Challenge Output

    5 -> 1/9, 9/8,  8/15, 15/7, 7/20, 20/13,  13/19, 19/6, 6/23, 23/17,  17/28, 28/11, 11/27, 27/16,  16/21, 21/5,
    5/24, 24/19,  19/33, 33/14, 14/37, 37/23,  23/32, 32/9, 9/31,  31/22, 22/35, 35/13, 13/30,  30/17, 17/21,
    21/4, 4/23, 23/19,  19/34, 34/15, 15/41, 41/26,  26/37, 37/11, 11/40, 40/29, 29/47,  47/18, 18/43, 43/25,
    25/32, 32/7, 7/31,  31/24, 24/41, 41/17, 17/44,  44/27, 27/37, 37/10, 10/33, 33/23,  23/36, 36/13, 13/29,
    29/16, 16/19, 19/3,  3/20, 20/17, 17/31, 31/14,  14/39, 39/25, 25/36, 36/11, 11/41,  41/30, 30/49, 49/19,
    19/46, 46/27, 27/35,  35/8, 8/37, 37/29, 29/50,  50/21, 21/55, 55/34, 34/47, 47/13,  13/44, 44/31, 31/49,
    49/18, 18/41, 41/23,  23/28, 28/5, 5/27, 27/22,  22/39, 39/17, 17/46, 46/29, 29/41,  41/12, 12/43, 43/31,
    31/50, 50/19,  19/45, 45/26, 26/33,  33/7, 7/30,  30/23, 23/39, 39/16,  16/41, 41/25, 25/34,  34/9, 9/29,
    29/20, 20/31,  31/11, 11/24, 24/13, 13/15,  15/2, 2/15, 15/13,  13/24, 24/11, 11/31, 31/20,  20/29, 29/9,
    9/34, 34/25,  25/41, 41/16, 16/39, 39/23,  23/30, 30/7, 7/33,  33/26, 26/45, 45/19, 19/50,  50/31, 31/43,
    43/12, 12/41, 41/29,  29/46, 46/17, 17/39, 39/22,  22/27, 27/5, 5/28, 28/23, 23/41,  41/18, 18/49, 49/31,
    31/44, 44/13, 13/47,  47/34, 34/55, 55/21, 21/50,  50/29, 29/37, 37/8, 8/35, 35/27,  27/46, 46/19, 19/49,
    49/30, 30/41, 41/11,  11/36, 36/25, 25/39, 39/14,  14/31, 31/17, 17/20, 20/3, 3/19,  19/16, 16/29, 29/13,
    13/36, 36/23, 23/33,  33/10, 10/37, 37/27, 27/44,  44/17, 17/41, 41/24, 24/31, 31/7,  7/32, 32/25, 25/43,
    43/18, 18/47, 47/29,  29/40, 40/11, 11/37, 37/26,  26/41, 41/15, 15/34, 34/19, 19/23,  23/4, 4/21, 21/17,
    17/30, 30/13,  13/35, 35/22, 22/31,  31/9, 9/32,  32/23, 23/37, 37/14,  14/33, 33/19, 19/24,  24/5, 5/21,
    21/16, 16/27, 27/11, 11/28, 28/17, 17/23, 23/6, 6/19, 19/13, 13/20, 20/7, 7/15, 15/8, 8/9, 9/1




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
