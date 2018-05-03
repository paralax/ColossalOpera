# Title

Regular Paperfold Sequence Generator

# Difficulty

Easy

# Tags

binary sequence, infinite sequence, math

# Description

In mathematics the [regular paperfolding sequence](https://en.wikipedia.org/wiki/Regular_paperfolding_sequence), also known as the dragon curve sequence, is an infinite automatic sequence of 0s and 1s. At each stage an alternating sequence of 1s and 0s is interleaved between the terms of the previous sequence. The first few generations of the sequence look like this:

	1
	1 1 0
	1 1 0 1 1 0 0
	1 1 0 1 1 0 0 1 1 1 0 0 1 0 0
	

The sequence takes its name from the fact that it represents the sequence of left and right folds along a strip of paper that is folded repeatedly in half in the same direction. If each fold is then opened out to create a right-angled corner, the resulting shape approaches the dragon curve fractal.

# Challenge Input

Your challenge today is to implement a regular paperfold sequence generator up to 8 cycles (it gets lengthy quickly). 

# Challenge Output

(With line breaks for readability)

	110110011100100111011000110010011101100111001000110110001100100111011001110010
	011101100011001000110110011100100011011000110010011101100111001001110110001100
	100111011001110010001101100011001000110110011100100111011000110010001101100111
	001000110110001100100111011001110010011101100011001001110110011100100011011000
	110010011101100111001001110110001100100011011001110010001101100011001000110110
	011100100111011000110010011101100111001000110110001100100011011001110010011101
	1000110010001101100111001000110110001100100

# FSharp Solution

	let rec paperfold (start:string) (rounds:int) : string = 
		let rec inserts n c acc = 
			match c with
			| 0 -> acc
			| _ -> match n with
				   | "0" -> inserts "1" (c-1) ("1"::acc)
				   | "1" -> inserts "0" (c-1) ("0"::acc)
		match rounds with
		| 0 ->  start
		| _ ->  let start = (start.ToCharArray() |> List.ofArray |> List.map string) @ ["X"]
			    let res = (List.zip (inserts "1" ((List.length start)) []) start
						 |> List.map (fun x -> (fst x) + (snd x))
						 |> String.concat "").Replace("X", "")
				paperfold res (rounds - 1)
