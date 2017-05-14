# Title

Longest Palindromic Substring

# Difficulty

Easy

# Tags

palindrome, substring

# Description

In computer science, the longest palindromic substring or longest symmetric factor problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome. 

For example, the longest palindromic substring of "bananas" is "anana". The longest palindromic substring is not guaranteed to be unique; for example, in the string "abracadabra", there is no palindromic substring with length greater than three, but there are two palindromic substrings with length three, namely, "aca" and "ada".

Remember - substrings must be contiguous strings contained within the string. For this challenge spaces are OK, capitalization doesn't matter. 

# Input Description

You'll be given inputs as one word per line. Example:

	bananas

# Output Description

Your program should emit any of the longest substrings it can find in the input word. Candidate palindromes must be longer than 1 letter. Example:

	anana

# Challenge Input

	zeallessness
	abastardize
	ureterocystoscope

# Challenge Output

	ss
	aba
	reter

# FSharp Solution

	let reverse (s:string) : string = s.ToCharArray() |> Array.map string |> Array.rev |> String.concat ""
	let palindrome (s:string) : bool = s = reverse s
	let substrings (s:string) : string list =
		let tails (s:string) : string list =  List.map (fun x -> s.[..x]) [0..(s.Length - 1)]	
		List.map (fun x -> tails (s.Substring(x))) [0..s.Length]
		|> List.concat

	let solution (s:string) : string = 
		substrings s 
		|> List.filter (fun x -> x.Length > 1) 
		|> List.filter palindrome 
		|> List.map (fun x -> (x.Length, x)) 
		|> List.sortBy fst 
		|> List.rev
		|> List.map snd 
		|> List.head
