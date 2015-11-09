# Title

Extravagant Numbers 

# Difficulty

Easy

# Description

An extravagant number (also known as a wasteful number) is a natural number that has fewer digits than the number of digits in its prime factorization (including exponents). Trivial examples include 6 = 2*3, 8 = 2^3, and 9 = 3^2, all extravagant numbers. 

Your challenge today is to write a program to determine is numbers are extravagant or not. 

# Input Description

You'll be given a single integer per line. Examples:

    6
    16
    32
    99

# Output Description

Your program should emit if the number is extravagant or not:

    6 EXTRAVAGANT
    16 NOT EXTRAVAGANT
    32 NOT EXTRAVAGANT
    99 EXTRAVAGANT

# Challenge Input

    90
    30
    74
    141
    782
    938

# Challenge Output

    90 EXTRAVAGANT
    30 EXTRAVAGANT
    74 EXTRAVAGANT
    141 NOT EXTRAVAGANT
    782 EXTRAVAGANT
    938 EXTRAVAGANT

# Scala Solution

    def factorize(x: Int): List[Int] = {
        @tailrec
        def foo(x: Int, a: Int = 2, list: List[Int] = Nil): List[Int] = a*a > x match {
          case false if x % a == 0 => foo(x / a, a    , a :: list)
          case false               => foo(x    , a + 1, list)
          case true                => x :: list
        }
        foo(x)
      }

    def power(n:Int): String = {
        if (n.toInt > 1) {return n.toString}
        else {return ""}
    }

    def extravagant(n:Int): Boolean = 
        factorize(n).groupBy(x => x).mapValues(_.length).map(x => x._1 + "" + power(x._2)).mkString("").length > n.toString.length
