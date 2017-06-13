# Title

Summing Across the Rudin-Shapiro Sequence 

# Difficulty

Easy

# Tags

math, integer sequence, binary

# Description

In mathematics the Rudin–Shapiro sequence, also known as the Golay–Rudin–Shapiro sequence is an infinite automatic sequence where each term of the Rudin–Shapiro sequence is either +1 or −1. The sequence is named after Marcel Golay, Walter Rudin and Harold S. Shapiro, who independently studied it.

The value of the term _b_n_, the _n_th term of the sequence, is -1 raised to the power _a_n_. The value of _a_n_, in turn, is the number of (possibly overlapping) "11" terms in the binary expansion of _n_. The first ten terms of the sequence _a_ are therefore:

	0 0 1 0 0 1 2 0 0 0

And the first ten terms of the sequence _b_ are:

	1 1 -1 1 1 -1 1 1 1 1

**Your challenge today is to implement a generator for the Rudin-Shapiro sequence and sum the first million terms.**

(For you number theory nerds out there you'll spot some interesting features of the sequence, such as how it converges, from the positive, to 0 as you expand further out. It also has no runs of -1 or +1 longer than 4.)

# Challenge Output

The first million terms (starting at 0 and ending at 999999) of the sequence sum to 1112. 

# Bonus Challenge

If you build a Rudin-Shapiro chain of sequences, concatenating the sequences for 1, then 2, then 3 and so forth ... what is the millionth term in that sequence? +1 or -1?

I get -1. 

# FSharp Solution

	let countSubstringsOf (needle:string) (haystack:string) : int = 
		let rec loop (n:string) (h:string) (c:int) : int = 
			match h.IndexOf(n) with
			| -1              -> c
			| x when (x >= 0) -> loop n (h.[x+1..]) (c+1)
		loop needle haystack 0
	let binary (n:int) : string = System.Convert.ToString(n, 2)
	let a (x:int) : int = countSubstringsOf "11" (binary x)
	let b (y:int) : float = System.Math.Pow(-1.0, float(y))
	let rudin_shapiro (n:int) : int list =
		[ 0..(n-1)] 
		|> List.map (fun x -> (binary x, a x)) 
		|> List.map (fun (x,y) -> (x, b y)) 
		|> List.map (fun (_,y) -> int(y))
	let solution (n:int) : int =
		rudin_shapiro n |> List.sum 
		
	let bonus (len:int) : int =
		let rec loop (n:int) (sofar:int list) : int list =
			match (List.length sofar) with
			| x when x > len -> sofar
			| _              -> loop (n+1) (sofar@(rudin_shapiro n))
		loop 0 (List.empty<int>)
		|> List.skip len
		|> List.head
