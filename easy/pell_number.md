# Title

Pell Numbers

# Difficulty

Easy

# Tags

number sequence, infinite sequence, number theory

# Description

In mathematics, the [Pell numbers](https://en.wikipedia.org/wiki/Pell_number) are an infinite sequence of integers, known since ancient times, that comprise the denominators of the closest rational approximations to the square root of 2. This sequence of approximations begins 1/1, 3/2, 7/5, 17/12, and 41/29, so the sequence of Pell numbers begins with 0, 1, 2, 5, 12, and 29 (each Pell number is the sum of twice the previous Pell number and the Pell number before that).

Your challenge today is to generate this sequence and pick out specific elements in the seqence. 

If you're feeling especially brave, try applying memoization and recursion in your answer. 

# Sample Input

You'll be given number *N*, one per line. This is the position in the sequence of Pell numbers to yield. Examples:

    3
    5

# Sample Output

    2
    12

# Challenge Input

    10
    17

# Challenge Output

    985
    470832

# Bonus

What is the 100th Pell number? (Answer: 27749033099085295754434173207717704165)

# F# Solution

    let pell n =
        let addPell a b = (2I*a + b)
        let rec loop n sofar = 
            printfn "%A" sofar
            match ((List.length sofar) = n) with
            | true  -> List.head sofar
            | false -> loop n ((addPell (List.head sofar) (Seq.nth 1 sofar))::sofar)
        match n with
        | 0 -> 0I
        | 1 -> 1I
        | _ -> loop n [1I; 0I]