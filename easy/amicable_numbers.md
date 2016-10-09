# Title

Finding Amicable Numbers

# Difficulty

Easy

# Tags

amicable numbers, math, number theory, numbers

# Description

In mathematics, amicable numbers are two distinct numbers related such that the sum of the proper divisors of each is equal to the other number. (A proper divisor of a number is a positive factor of that number other than the number itself. For example, the proper divisors of 6 are 1, 2, and 3.) Amicable numbers were known to the Pythagoreans, who credited them with many mystical properties.

The smallest pair of amicable numbers is (220, 284). They are amicable because the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; and the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.

As of April 2016, there are over 1,000,000,000 known amicable pairs. For more information see the OEIS sequence [A259180](https://oeis.org/A259180). 

# Input Description

You'll be given numbers, one on a line. Example:

    220

# Output Description

Your program should emit the number's amicable pairing along with the proper divisors for both. Example:

    284: 1 2 4 71 142
    220: 1 2 4 5 10 11 20 22 44 55 110

# Challenge Input

    10744
    12285
    63020

# Challenge Output

    10744: 1 2 4 8 17 34 68 79 136 158 316 632 1343 2686 5372
    10856: 1 2 4 8 23 46 59 92 118 184 236 472 1357 2714 5428

----

    12285: 1 3 5 7 9 13 15 21 27 35 39 45 63 65 91 105 117 135 189 195 273 315 351 455 585 819 945 1365 1755 2457 4095
    14595: 1 3 5 7 15 21 35 105 139 417 695 973 2085 2919 4865

----

    63020: 1 2 4 5 10 20 23 46 92 115 137 230 274 460 548 685 1370 2740 3151 6302 12604 15755 31510
    76084: 1 2 4 23 46 92 827 1654 3308 19021 38042

# Fsharp Solution

    let proper_divisors (n:int) : int list = 
        List.filter (fun x -> n%x = 0) [1..(n-1)]

    let amicable (n:int) : int = 
        proper_divisors n |> List.sum

    let solution (n:int) = 
        let t = amicable n
        printf "%d: " n
        proper_divisors n |> List.iter (fun x -> printf "%d "  x )
        printfn ""
        printf "%d: " t
        proper_divisors t |> List.iter (fun x -> printf "%d "  x )
        printfn ""

    // to find amicable numbers up to a point ...
    [1..1000] 
    |> List.map (fun x -> [amicable x; x])
    |> List.filter (fun [x; y] -> (amicable x) = y)
    |> List.map List.sort
    |> Seq.distinct  
    |> Seq.filter (fun [x; y] -> x <> y) 
    |> Seq.map (fun [x;y] -> (x,y))