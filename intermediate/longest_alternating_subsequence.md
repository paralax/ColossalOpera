# Title

Longest Alternating Subsequence

# Difficulty

Intermediate

# Tags

subsequence

# Description

In the longest alternating subsequence problem, one wants to find a subsequence of a given sequence in which the elements are in alternating order, and in which the sequence is as long as possible. 

Remember, a subsequence of a given sequence is a sequence formed from the given sequence by deleting some of the elements without disturbing the relative positions of the remaining elements. For instance, the sequence of positive even integers (2, 4, 6, ...) is a subsequence of the positive integers (1, 2, 3, ...). The positions of some elements change when other elements are deleted. However, the relative positions are preserved.

We denote the function *as* as *as_n* where *n* is the number of elements in the sequence. The value of the function is the length of the longest alternating subsequence. Some examples:

* as_5(1,2,3,4,5) = 2 because any sequence of 2 distinct digits are (by definition) alternating. (for example 1,2 or 1,4 or 3,5)
* as_5(1,5,3,2,4) = 4 because 1,5,3,4 and 1,5,2,4 and 1,3,2,4 are all alternating, and there is no alternating subsequence with more elements
* as_5(5,3,4,1,2) = 5 because 5,3,4,1,2 is itself alternating

# Input Description

You'll be given a sequence of integers, one sequence per line. Example:

	10  22  9  33  49  50  31  60

# Output Descripton

Your program should emit the length of the longest alternating subsequence. From the above example:

	10  22  9  33  49  50  31  60 -> 6

(This is because a subsequence like `10  22  9  33  31  60` is a six member alternating subsequence.)

# Challeng Input 

	1 5 4
	1 4 5
	13 18 3 8 16 12 6 7 11 1 2 19 4 15 17 5 0 9 14 10
	9 5 7 1 6 4 0 2 8 3

# Challenge Output

	1 5 4 -> 3
	1 4 5 -> 2
	13 18 3 8 16 12 6 7 11 1 2 19 4 15 17 5 0 9 14 10 -> 16
	9 5 7 1 6 4 0 2 8 3 -> 9

# FSharp Solution

	let longestSubsequence(s:seq<int>) : int =
		let getSigns(s:seq<int>) : seq<int> =
			Seq.windowed 2 s |> 
			Seq.map (fun [|x;y|] -> Operators.compare x y)

		let targetSequence (n:int) : seq<int> = 
			let rec loop (n:int) (acc:int list): int list =
				if n = 0 then acc
				else
					match (Seq.last acc) with
					| -1 -> loop (n-1) (acc@[1])
					|  1 -> loop (n-1) (acc@[-1])
			loop (n-1) [1] |> Seq.ofList

		// http://www.clear-lines.com/blog/post/Longest-Common-Subsequence-in-F-Sharp.aspx
		let rec LCS list1 list2 =
		  if List.length list1 = 0 || List.length list2 = 0 then
		    List.Empty
		  else
		    let tail1 = List.tail list1
		    let tail2 = List.tail list2
		    if List.head list1 = List.head list2 then
		      List.head list1 :: LCS tail1 tail2
		    else
		      let candidate1 = LCS list1 tail2
		      let candidate2 = LCS tail1 list2
		      if List.length candidate1 > List.length candidate2 then
		        candidate1
		      else
		        candidate2
		1 + (LCS ( getSigns s |> List.ofSeq) ( targetSequence (Seq.length s - 1) |> List.ofSeq) |> List.length)
