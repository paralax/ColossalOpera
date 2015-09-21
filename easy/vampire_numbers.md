# Title 

Vampire Numbers

# Difficulty

Easy

# Description

A vampire number *v* is a number *v=xy* with an even number *n* of digits formed by multiplying a pair of *n*/2-digit numbers (where the digits are taken from the original number in any order) *x* and *y* together. Pairs of trailing zeros are not allowed. If *v* is a vampire number, then *x* and *y* are called its "fangs." 

Additional information can be found here: http://www.primepuzzles.net/puzzles/puzz_199.htm

# Input Description

Two digits on one line indicating *n*, the number of digits in the number to factor and find if it is a vampire number, and *m*, the number of fangs. Example:

    4 2

# Output Description

A list of all vampire numbers of *n* digits, you should emit the number and its factors (or "fangs"). Example:

    1260=21*60
    1395=15*93
    1435=41*35
    1530=51*30
    1827=87*21
    2187=27*81
    6880=86*80

# Challenge Input

    6 3

# Challenge Input Solution 

    114390=41*31*90
    121695=21*61*95
    127428=21*74*82
    127680=21*76*80
    127980=20*79*81
    137640=31*74*60
    139500=31*90*50
    163680=66*31*80
    178920=71*90*28
    197925=91*75*29
    198450=81*49*50
    247680=40*72*86
    294768=46*72*89
    376680=73*60*86
    397575=93*75*57
    457968=56*94*87
    479964=74*94*69
    498960=99*84*60



# Scala solution

    object VampireNumbers {
      def product(list: List[Int]): Int = list.foldLeft(1)(_*_)

      def vampire(n:Int, fangs:Int):List[(Int, List[Int])] ={
        n.
         toString.
         map(_.toString.toInt).
         permutations.
         map(_.grouped(2).map(_.mkString.toInt).toList).
         map(x=>(product(x),x)).
         filter(_._1==n).
         toList
      }

      def main(argc:Int, argv:Array[String]) = {
        val start = scala.math.pow(10, argv(1).toInt-1).toInt
        val end = scala.math.pow(10, argv(1).toInt).toInt-1
        val fangs = argv(2).toInt
        (start to end).map(x => vampire(x, fangs)).filter(_.length > 0).foreach(println)
      }
    }
