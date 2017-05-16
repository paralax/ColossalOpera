# Title

3SUM

# Difficulty

Easy

# Tags

complexity

# Description

In computational complexity theory, the 3SUM problem asks if a given set of *n* real numbers contains three elements that sum to zero. 

# Input Example

You will be given a list of integers, one set per line. Example:

	9 -6 -5 9 8 3 -4 8 1 7 -4 9 -9 1 9 -9 9 4 -6 -8

# Output Example

Your program should emit triplets of numbers that sum to 0. Example:

	-9 1 8
	-8 1 7
	-5 -4 9
	-5 1 4
	-4 1 3

# Challenge Input

	4 5 -1 -2 -7 2 -5 -3 -7 -3 1
	-1 -6 -3 -7 5 -8 2 -8 1
	-5 -1 -4 2 9 -9 -6 -1 -7

# Challenge Output

	-7 2 5
	-5 1 4
	-3 -2 5
	-3 -1 4
	-3 1 2
	
	-7 2 5
	-6 1 5
	-3 1 2
	
	-5 -4 9

# FSharp Solution

	let choose k ns =
	    let rec fC prefix m from = seq {
	        let rec loopFor f = seq {
	            match f with
	            | [] -> ()
	            | x::xs ->
	                yield (x, fC [] (m-1) xs)
	                yield! loopFor xs
	        }
	        if m = 0 then yield prefix
	        else
	            for (i, s) in loopFor from do
	                for x in s do
	                    yield prefix@[i]@x        
	    }
	    fC [] k ns
	
	let solution ns =
		choose 3 ns 
		|> Seq.map (fun x -> (x, List.sum x)) 
		|> Seq.filter (fun (x,y) -> y = 0) 
		|> Seq.map (fun (x,_) -> Set.ofSeq x) 
		|> Set.ofSeq 
		|> Set.toSeq 
		|> Seq.iter (fun x -> printfn "%A " x)
