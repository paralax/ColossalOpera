# Title

Abundant and Deficient Numbers

# Difficulty

Easy

# Tags

number theory

# Description

In number theory, a deficient or **deficient number** is a number n for which the sum of divisors *sigma(n)<2n*, or, equivalently, the sum of proper divisors (or aliquot sum) *s(n)<n*. The value *2n - sigma(n)* (or *n - s(n)*) is called the number's deficiency. In contrast, an **abundant number** or excessive number is a number for which the sum of its proper divisors is greater than the number itself

As an example, consider the number 21. Its divisors are 1, 3, 7 and 21, and their sum is 32. Because 32 is less than 2 x 21, the number 21 is *deficient*. Its deficiency is 2 x 21 - 32 = 10.

The integer 12 is the first *abundant* number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16. The amount by which the sum exceeds the number is the abundance. The number 12 has an abundance of 4, for example. 

#  Input Description

You'll be given an integer, one per line. Example:

    18
    21
    9

#  Output Description

Your program should emit if the number if deficient, abundant (and its abundance), or neither. Example:

    18 abundant by 3
    21 deficient
    9 neither 

# Challenge Input

    111  
    112 
    220 
    69 
    134 
    85 

# Challenge Output

    111 neither 
    112 abundant by 24
    220 abundant by 64
    69 deficient
    134 deficient
    85 deficient

# Scala Solution

    def divisors(n: Int): List[Int] = for (i <- List.range(1, n) if n % i == 0) yield i
    def abundance(n:Int): Int = divisors(n).sum-n
    def abundant(n:Int): Boolean = divisors(n).sum > n
    def deficient(n:Int): Boolean = 2*divisors(n).sum < n
    def main(n:Int): String = {
        if (abundant(n)) {
            return "abundant by " + abundance(n)
        }
        if (deficient(n)) {
            return "deficient"
        }
        return "neither"
    }
