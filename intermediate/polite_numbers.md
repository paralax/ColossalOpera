# Title

Finding Numbers with Manners

# Difficulty

Intermediate

# Description

In number theory, a polite number is a positive integer that can be written as the sum of two or more consecutive positive integers. 3 is a polite number because `1 + 2 = 3`. 4 is not a polite number - it's an impolite number - because you cannot add any two consecutive numbers to yield a sum of 4. It turns out the impolite numbers are exactly the powers of two.

Furthermore, the *politeness* of a number is how many different arrangements of consecutive integers can sum to the given number. For instance, 9 has a politeness of 2 because:

    9 = 2 + 3 + 4 = 4 + 5

For every x, the politeness of x equals the number of odd divisors of x that are greater than 1. An easy way of calculating the politeness of a positive number is that of decomposing the number into its prime factors, taking the powers of all prime factors greater than 2, adding 1 to all of them, multiplying the numbers thus obtained with each other and subtracting 1.

#  Input Description

You'll be given a row with a single integer *N* that tells you how many numbers to read. Then you'll be given *N* lines of integers to determine the politeness for. Example:

    3
    3
    8
    90

# Output Description

Your program should emit the number and its politeness. Example:

    3 -> 1
    8 -> 0
    90 -> 5

# Challenge Input

    10
    42
    87
    3197
    200
    546
    38
    39
    19
    99
    34

# Challenge Output

    42 -> 3
    87 -> 3
    3197 -> 3
    200 -> 2
    546 -> 7
    38 -> 1
    39 -> 3
    19 -> 1
    99 -> 5
    34 -> 1

# Bonus

Find the largest politeness of numbers below 10000. 

# Scala Solution

    def politeness(n:Int): Int = {
        def loop(n:Int, len:Int, windows:List[Int], sofar:List[Int]): List[Int] = {
            if (len == n) { return sofar }
            else {return loop(n, len+1, windows, windows.sliding(len).map(_.sum).filter(_==n).toList++sofar)}
        }
        if (n < 3) {0}
        else {loop(n, 2, (1 to (n - 1)).toList, List()).length}
    }
