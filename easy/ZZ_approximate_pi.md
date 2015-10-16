# Title 

Approximate PI

# Difficulty

Easy

# Description

The mathematical constant pi - the ratio of a circle's circumference to its radius - is an irrational number. Approximations have been made - first by hand and now by computers - for over 4000 years. The current record is to 12.1 trillion digits!

Approximations start to fail after various decimal places. For instance, the simple "25/8" approximation is good to only 2 decimal places, while "62832/20000" is correct to 4 decimal places. Various algorithms have been developed over the years that provide increasing accuracy.

For this challenge your task is to implement one or more of those algorithms and approximate pi correctly to a specific number of digits. You may *NOT* for this challenge use your programming language or system's built in definitions of pi (e.g. System.Math.PI from .Net, or M_PI from math.h), you should not solve it using geometric functions like `sin()` or `tan()` or the like, or "find it" by downloading it from somewhere - that's straight up cheating. 

# Challenge Input

You'll be given *N*, a number of digits to which to correctly approximate pi. 

        4  (should be 3.1415 or 3.1416)
        6  (should be 3.141592 or 3.141593) 
        10 (should be 3.1415926535)

# Notes

User /u/skeeto had submitted a similar one before based on a specific approximation method: http://www.reddit.com/r/dailyprogrammer_ideas/comments/1qrrpa/easy_buffons_needle_pi_estimation/

# Scala Solution

    def factorial(n:Int):Int = if (n==0) 1 else n * factorial(n-1)

    def Ramanujan_Series(k:Int, sofar:Double): Double = {
        k match {
            case -1 => 1/(12*sofar)
            case _  => Ramanujan_Series(k - 1, sofar + ((math.pow(-1.0, k.toDouble) * factorial(6 * k) * (13591409 + 545140134 * k))/
             (factorial(3 * k) * math.pow(factorial(k), 3.0) * math.pow(640320, (1.5 + 3 * k)))))
         }
    }  
