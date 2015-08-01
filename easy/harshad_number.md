# Title

Harshad Number 

# Difficulty

Easy

# Description

In recreational mathematics, a Harshad number (or Niven number) in a given number base, is an integer that is divisible by the sum of its digits when written in that base. Thus, you can observe that number 21 is indeed a Harshad number.

# Input Description

You'll be given an integer, one per line. Example:

    21
    22

# Output Description

Your program should emit if the number is a Harshad number or not. Example:

    21 HARSHAD
    22 NOT HARSHAD

# Challenge Input

    21
    49
    62
    63

# Challenge Output

    21 HARSHAD 
    49 NOT HARSHAD
    62 NOT HARSHAD
    63 HARSHAD

# Scala Solution

    def harshad(n:Int): Boolean = (n/n.toString.toCharArray.map(_.toString.toInt).sum)*(n.toString.toCharArray.map(_.toString.toInt).sum) == n
