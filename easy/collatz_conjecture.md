# Title

Collatz Conjecture

# Difficulty

Easy

# Tags

number theory, infinite sequence, integer sequence

# Description

The [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) is a conjecture in mathematics named after Lothar Collatz, who first proposed it in 1937. Take any natural number n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process (which has been called "Half Or Triple Plus One", or HOTPO) indefinitely. The conjecture is that no matter what number you start with, you will always eventually reach 1.

For instance, starting with n = 6, one gets the sequence 6, 3, 10, 5, 16, 8, 4, 2, 1. n = 19, for example, takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

# Input 

Your program should take a positive integer *N* as an argument.

# Output Description

Your program should emit the number of steps it takes to reach 1 and the sequence emitted.

# Bonus 1

Can you explain what's so interesting about the number 9232 in the context of the Collatz Conjecture?

# Bonus 2

If you're feeling like it, throw in some unique visualizations of sequences or series from the Collatz Conjecture, using any imaging library you wish. 


# Scala Solution

    def collatz(N:Int): List[Int] = {
      def loop(n:Int, sofar:List[Int]): List[Int] = {
        n match {
          case 1 => 1::sofar
          case _ => (n%2 == 0) match {
              case true => loop(n/2, n::sofar)
              case false => loop(1 + 3*n, n::sofar)
          }
        }
      }
      loop(N, List()).reverse
    }
