# Title

Getting To A Set Of 8 Numbers 

# Difficulty 

Easy

# Tags

math, number theory

# Description

Mathematician Arthur Porges in 1945 published a paper about a simple mathematical formula. Take any number *N* and then take the sum of its digits squared, and repeat that process. You'll continually come to this loop: 4 16 37 58 89 145 42 20. 

Your task today is to take a given number and then calculate how far away it is from this loop - this set of 8 numbers - it is. Any number in the loop sequence will suffice (e.g. if you land on 89 and not 4 you've officially hit the loop). 

# Input Description

You'll be given a single integer per line. Example:

    187597

# Output Description

Your program should emit the length of the sequence to enter the set of 8 numbers. Example:

    187597 -> 11

Optionally show the numbers it took to gett here.

# Challenge Input

    2081761
    97
    918767

# Challenge Output

    2081761 -> 4
    97 -> 2
    918767 -> 3

# Bonus

What's the longest chain length you can find up to 999999. 

# Notes 

http://fermatslibrary.com/s/a-set-of-eight-numbers

# FSharp Solution

For some reason I have to also catch the case of "1", otherwise it goes on forever. Perhaps I should work harder to understand the paper. 

    let solution (n:int) = 
        let _porges (n:int) : int =
            (string n).ToCharArray()
            |> Array.map string
            |> Array.map int
            |> Array.map (fun x -> x * x)
            |> Array.sum
        let rec _loop n c =
            let nn = _porges n
            match nn with
            | 1 | 4 | 16 | 37 | 58 | 89 | 145 | 42 | 20 -> c
            | _ -> _loop nn (c+1)
        printfn "%d -> %d" n (_loop n 0)
