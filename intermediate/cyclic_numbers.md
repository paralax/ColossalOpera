# Title

Constructing Cyclic Numbers

# Difficulty

Intermediate

# Tags

math, cyclic numbers

# Description

A [cyclic number](https://en.wikipedia.org/wiki/Cyclic_number) is an integer in which cyclic permutations of the digits are successive multiples of the number. The most widely known in base 10 is 142857:

    142857 * 1 = 142857
    142857 * 2 = 285714
    142857 * 3 = 428571
    142857 * 4 = 571428
    142857 * 5 = 714285
    142857 * 6 = 857142

You can watch the `714` loop through the number again and again, showing you the cycle.

Cyclic numbers can be constructed using the following steps: 

1. Let *b* be the number base (e.g. 10 for decimal)
1. Let *p* be a prime that does not divide *b*.
1. Let *t* = 0.
1. Let *r* = 1.
1. Let *n* = 0.
1. Loop over the following steps:
    1. Let *t* = *t* + 1
    1. Let *x* = *r* * *b*
    1. Let *d* = int(*x*/*p*)
    1. Let *r* = *x* mod *p*
    1. Let *n* = *n* * *b* + *d*
    1. If r != 1 then repeat the loop.
1. if *t* = *p* - 1 then n is a cyclic number.

Your challenge today is a bit different than a typical challenge. Instead of creating or hunting for an algorithm, your challenge is to *implement* the above algorithm and create some cyclic numbers. 

# Note

Implementing an algorithm from a description is a valuable skill to have, just as is designing an algorithm. That's why this is a programming challenge - not solving a puzzle, but applying your language knowledge to a problem. 

# Scala Solution

    def makeCyclic(b:Int, p:Int): Int = {
        var t = 0
        var r = 1
        var n = 0
        def loop(n: Int, t:Int, r:Int, b:Int): Int = {
            val tt = t + 1
            val x = r * b
            val d = x/p
            var nn = n * b * d
            r match {
                case 1 => t
                case _ => loop(nn, t, r, b)
            }
        }
        t = loop(n, t, r, b)
        if (t == p - 1) {
            return t
        } else {
            return -1
        }
    }
