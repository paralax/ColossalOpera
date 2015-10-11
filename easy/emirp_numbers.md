# Title

Emirp Numbers 

# Difficulty

Easy

# Description

We all know what prime numbers are - numbers only divisible by themselves and one. Math grad student Matthew Scroggs came up with *emirp* numbers. An emirp number is a prime number which is a different prime number when the digits are reversed.

Your task today is to write a program that can discover emirp numbers over a range. 

# Input Description

You'll be given two numbers, *a* and *b*, that represent the range *inclusive* of the numbers to screen for emirp numbers. Example:

    10 100

# Output Description

Your program should emit the list of valid emirp numbers for that range. Example:

    [11; 13; 17; 31; 37; 71; 73; 79; 97]

# Challenge Input

    10000 10100
    999810 999999
    
# Challenge Output

    [10007; 10009; 10039; 10061; 10067; 10069; 10079; 10091]
    [999853; 999931; 999983]

# FSharp Solution

    let isprime (n:int) =
        let rec check i =
            i > n/2 || (n % i <> 0 && check (i + 1))
        check 2;;

    let revnum(n:int) = 
        string(n).ToCharArray() |> Array.rev |> Array.map(fun x -> string(x)) |> String.concat "" |> int


    [ 1 .. 100 ] |> List.filter isprime |> List.filter (fun x -> revnum x |> isprime)
