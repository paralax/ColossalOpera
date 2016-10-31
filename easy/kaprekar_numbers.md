# Title

[2016-10-31] Challenge #290 [Easy] Kaprekar Numbers

# Difficulty

Easy

# Tags

number theory, Kaprekar

# Description

In mathematics, a [Kaprekar number](https://en.wikipedia.org/wiki/Kaprekar_number) for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 452 = 2025 and 20+25 = 45. The Kaprekar numbers are named after D. R. Kaprekar. 

I was introduced to this after the recent [Kaprekar constant challenge](https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/). 

For the main challenge we'll only focus on base 10 numbers. For a bonus, see if you can make it work in arbitrary bases.

# Input Description

Your program will receive two integers per line telling you the start and end of the range to scan, inclusively. Example:

	1 50

# Output Description

Your program should emit the Kaprekar numbers in that range. From our example:

	45

# Challenge Input

	2 100
	101 9000

# Challenge Output

	45 55 99
	297 703 999 2223 2728 4879 5292 7272 7777

# Fsharp Solution

	let kaprekar (n:int) = 
		let chunked(s:string) : seq<string list> =
			let n = s.Length
			seq { for i in 0..(n-2) do yield [s.[0..i] s.[(i+1)..(n-1)]]}
		let sum_pieces(s: string) =
			chunked s |> Seq.map (fun x -> List.map int x) |> Seq.map List.sum
		[1..n+1] 
		|> List.map (fun x -> (x, sum_pieces (string(x*x))))
		|> List.map (fun (x,y) -> (x, Seq.exists (fun j -> j = x) y))
		|> List.filter (fun (_,y) -> y)
		|> List.map fst
		|> List.filter (fun x -> x%10 <> 0)
	
	let solution (start:int) (_end:int) : int list =
		kaprekar _end |> List.filter (fun x -> x > (start-1))
