# Title

Baum-Sweet Sequence

# Difficulty

Easy

# Description

In mathematics, the Baum–Sweet sequence is an infinite automatic sequence of 0s and 1s defined by the rule:

* b_n = 1 if the binary representation of n contains no block of consecutive 0s of odd length;
* b_n = 0 otherwise;

for n ≥ 0.

For example, b_4 = 1 because the binary representation of 4 is 100, which only contains one block of consecutive 0s of length 2; whereas b_5 = 0 because the binary representation of 5 is 101, which contains a block of consecutive 0s of length 1. When n is 19611206, b_n is 0 because:

    19611206 = 1001010110011111001000110 base 2
                00 0 0  00     00 000  0 runs of 0s
                   ^ ^            ^^^    odd length sequences
               
Because we find an odd length sequence of 0s, b_n is 0. 
 
# Challenge Description

Your challenge today is to write a program that generates the Baum-Sweet sequence from 0 to some number *n*. For example, given "20" your program would emit:

    1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0

https://en.wikipedia.org/wiki/Baum%E2%80%93Sweet_sequence

# Scala Solution

    def b(n:Int): Int = {
        if (0 == n) {return 1}
        if (n.toBinaryString.split("1").filter(_!="").map(_.length%2 != 0).contains(true)) {return 0}
        else {return 1}
    }

    def baum_sweet(n:Int): IndexedSeq[Int] = (0 to n).map(b)
