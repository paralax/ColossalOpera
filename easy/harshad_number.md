# Title

Harshad Number 

# Difficulty

Easy

# Description

In recreational mathematics, a Harshad number (or Niven number) in a given number base, is an integer that is divisible by the sum of its digits when written in that base. Harshad numbers in base n are also known as *n*-Harshad (or *n*-Niven) numbers. Harshad numbers were defined by D. R. Kaprekar, a mathematician from India. The word "Harshad" comes from the Sanskrit *harṣa* (joy) + *da* (give), meaning joy-giver. The term “Niven number” arose from a paper delivered by Ivan M. Niven at a conference on number theory in 1977.

Thus, you can observe that number 21 is a Harshad number - 21 / (2 + 1) = 7. 

Today's challenge is to determine if an integer is a valid Harshad number. 

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

    def harshad(n:Int): Boolean = (n/n.toString.map(_.toString.toInt).sum)*(n.toString.map(_.toString.toInt).sum) == n
