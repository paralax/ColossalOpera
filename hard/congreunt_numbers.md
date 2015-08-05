# Title

Congruent Numbers

# Difficulty

Intermediate

# Description

In mathematics, a congruent number is a positive integer that is the area of a right triangle with three rational number sides. 6 is a congruent number because it is the area of a 3,4,5 triangle. The question of determining whether a given rational number is a congruent number is called the congruent number problem. 

This problem has not (as of 2012) been brought to a successful resolution. Dr Dobb's Journal recently (2009) posted a ["Lousy Algorithm"](http://www.drdobbs.com/architecture-and-design/congruent-numbers-and-the-lousy-algorith/228701878) for finding most congruent numbers under 100. While not perfect, it illustrates a strategy for determining if a number is congruent. There's a great discussion on the [bit-player blog](http://bit-player.org/2009/congruent-numbers) discussing various strategies to solve this challenge. 

Your challenge today is to determine if a given number is congruent or not. 

# Input Description

You'll be given an integer, one per line. Example:

    23
    12

# Output Description

Your program should emit if the number is congruent or not. Example:

    23 CONGRUENT
    12 NOT CONGRUENT

# Challenge Input

    6
    14
    44
    46
    29

# Challenge Output

    6 CONGRUENT
    14 CONGRUENT
    44 NOT CONGRUENT
    46 CONGRUENT
    29 CONGRUENT

# Scala Solution

    def pythagorean(a:Int, b:Int, c:Int) = (a*a + b*b) == (c*c)
    def congruent(a:Int, b:Int, c:Int) = if (pythagorean(a,b,c)) { (a*b)/2 } else {-1}