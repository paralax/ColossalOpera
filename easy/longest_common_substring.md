# Title

Longest Common Substring

# Difficulty

Easy

# Tags

substring

# Description

In computer science, the longest repeated substring problem is the problem of finding the longest substring of a string that occurs at least twice. These strings can't overlap, however. 

# Input Description

You'll be given inputs as one string per line. The strings may be a sentence. Example:

	bananas

# Output Description

Your program should emit the longest common substring found within the word. Example:

	 an

# Challenge Input

	the quick brown fox jumps over the lazy dog
	four score and seven years ago our fathers brought forth, upon this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.

# Challenge Output

	"the "
	"ated "

# Bonus

My solution is naive and takes a lot of time for longer inputs. Work on the most efficient implementation you can.

# FSharp Solution

	let substrings (s:string) : string list =
	    let tails (s:string) : string list =  List.map (fun x -> s.[..x]) [0..(s.Length - 1)]
	    List.map (fun x -> tails (s.Substring(x))) [0..s.Length]
	    |> List.concat

	let lcs (a:string) (b:string) : string = 
		let aa = Set.ofList (substrings a)
		let bb = Set.ofList (substrings b)
		let ss = Set.intersect aa bb
	  			 |> Set.map (fun x -> (x, x.Length))
	 			 |> Seq.sortBy snd
				 |> List.ofSeq
		match ss with
		| [] -> ""
		| _  -> List.map fst ss |> Seq.last

	let solution (s:string) : string * int = 
		[1..(s.Length-2)] 
		|> List.map (fun x -> (s.[0..x-1], s.Substring(x)))
		|> List.map (fun (x,y) -> lcs x y)
		|> List.map (fun x -> (x, x.Length))
		|> List.sortBy snd
		|> List.rev
		|> List.head
