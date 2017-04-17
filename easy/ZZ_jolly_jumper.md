# Title

[2017-04-17] Challenge #311 [Easy] Jolly Jumper

# Difficulty

Easy

# Tags

word play

# Description

A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values through n - 1 (which may include negative numbers). For instance,

    1 4 2 3

is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a jolly jumper.

# Input Description

You'll be given a row of numbers. The first number tells you the number of integers to calculate over, *N*, followed by *N* integers to calculate the differences. Example:

    4 1 4 2 3
    8 1 6 -1 8 9 5 2 7

# Output Description

Your program should emit some indication if the sequence is a jolly jumper or not. Example:

    4 1 4 2 3 JOLLY
    8 1 6 -1 8 9 5 2 7 NOT JOLLY

# Challenge Input

	4 1 4 2 3
	5 1 4 2 -1 6
	4 19 22 24 21
	4 19 22 24 25
	4 2 -1 0 2

# Challenge Output

	4 1 4 2 3 JOLLY
	5 1 4 2 -1 6 NOT JOLLY
	4 19 22 24 21 NOT JOLLY
	4 19 22 24 25 JOLLY
	4 2 -1 0 2 JOLLY

# FSharp Solution

	let jolly (s:string) : string = 
		let differences (s:string) : int list = 
			s.Split(' ').[1..] 
			|> Array.map (fun x -> int x) 
			|> Seq.windowed 2 
			|> Seq.map (fun [|x;y|] -> System.Math.Abs(x-y)) 
			|> Seq.sort
			|> List.ofSeq

		let target (s:string) : int list =
			let n = s.Split(' ').[0] |> int
			[(n-n+1)..(n-1)] 
		match (differences s) = (target s) with
		| true  -> "JOLLY"
		| false -> "NOT JOLLY"
