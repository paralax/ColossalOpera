# Title

Evil Numbers

# Difficulty

Easy

# Tags

number theory, binary 

# Difficulty

In number theory, an evil number is a non-negative number that has an even number of 1s in its binary expansion.

# Input Description

You'll be given a single number *N* per line telling you the maximum number to search for to find the three largest evil numbers. Example:

    40

# Output Description

Your program should emit the three largest evil numbers up to *N*. Example:

    34 36 39

# Challenge Input

    999
    18711

# Challenge Output

    994 996 999
    18707 18709 18710

# Fsharp Solution

    open System
    
    let solution (n:int) = 
        let evil (n:int) : bool = 
            Convert.ToString(n, 2).Replace("0", "").Length % 2 = 0
        [ 1..n ] 
        |> List.filter evil 
        |> List.rev 
        |> Seq.take 3 
        |> List.ofSeq 
        |> List.rev
        |> List.iter (fun x -> printf "%d " x )