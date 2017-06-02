# Title

Subset Sum Automata

# Difficulty

Hard

# Tags

automata, subset sum

# Description

We recently did the [subset sum](https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/) problem wherein given a sequence of integers, can you find any subset that sums to 0. Today, inspired by [this post](https://thquinn.github.io/projects/automaton.html) let's play subset sum automata. It marries the subset sum problem with [Conway's Game of Life](https://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/). 

You begin with a board full of random integers in each cell. Cells will increment or decrement based on a simple application of the subset sum problem: if any subset of the 8 neighboring cells can sum to the target value, you increment the cell's sum by some value; if not, you decrement the cell by that value. Automata are defined with three integers `x/y/z`, where `x` is the target value, `y` is the reward value, and `z` is the penalty value. 

# FSharp Solution

	// D generate board
	// D iterate over each square finding NW,N,NE,E,SE,S,SW,W values 
	// D apply subset sum to those values with target
	// D increment or penalize the cell as needed
	// D draw the board with color
	// Read and parse specification  

	open System			

	let colorMap : Map<int,ConsoleColor> = 
		Array.zip [|0..15|] [|ConsoleColor.Black; ConsoleColor.DarkBlue; ConsoleColor.DarkGreen; ConsoleColor.DarkCyan; ConsoleColor.DarkRed; ConsoleColor.DarkMagenta; ConsoleColor.DarkYellow; ConsoleColor.Gray; ConsoleColor.DarkGray; ConsoleColor.Blue; ConsoleColor.Green; ConsoleColor.Cyan; ConsoleColor.Red; ConsoleColor.Magenta; ConsoleColor.Yellow; ConsoleColor.White|]
		|> Map.ofArray

	let hasSubsetSum S (numbers: int array) =
	   if numbers |> Array.exists (fun x -> x = S) then
	     true
	   else
	     let a = numbers |> Array.filter (fun x -> x < S)      
	     let n = a.Length
	     if n = 0 then
	       false
	     else
	       let v = Array2D.create n (S+1) 0
	       let u = Array2D.create n (S+1) false
	       let t = Array2D.create n (S+1) 0

	       for j in [1..S] do
	         for i in [0..n-1] do                           
	           if j - a.[i] >= 0 && not u.[i,j - a.[i]] then
	             v.[i,j] <- t.[i,j - a.[i]] + a.[i]
	           if ((i = 0) || (i > 0 && t.[i-1,j] <> j)) && v.[i,j] = j then
	             u.[i,j] <- true
	           if v.[i,j] = j then
	             t.[i,j] <- j
	           else
	             if i > 0 then
	               t.[i,j] <- max t.[i-1,j] t.[i,j-1]
	             else
	               t.[i,j] <- t.[0,j-1]
       
	       t.[n-1,S] = S

	let rnd = new System.Random()
	let board (n:int) (m:int) : int [,] = 
		//	n x n board with m as max value
		let arr = Array2D.zeroCreate<int> n n
		for x in [0..(n-1)] do
			for y in [0..n-1] do
				arr.[x,y] <- rnd.Next() % m
		arr

	let size (arr:int[,]): int = arr.GetLength 0
	let wrap (arr:int [,]) (n:int) (off:int): int =
		let l = size arr
		match n + off with
		| x when x < 0 -> x + l
		| x when x > l -> (x+l) % l
		| _            -> n + off
	let neighbors (arr:int [,]) (x:int) (y:int): int list =
		let res = [ for xs in [-1;0;1] do
						for ys in [-1;0;1] do			
						   yield arr.[(wrap arr x xs), (wrap arr y ys)] ]
	    // skip the x,y cell we're on 
		(List.take 4 res)@(List.skip 5 res)

	let alter (arr: int [,]) (x:int) (y:int) (v:int): int [,] =
		arr.[x,y] <- arr.[x,y] + v 
		arr

	let reward (arr: int [,]) (x:int) (y:int) (v:int): int [,] =
		arr.[x,y] <- System.Math.Min(arr.[x,y] + v, 20)
		arr

	let penalize (arr: int [,]) (x:int) (y:int) (v:int): int [,] =
		arr.[x,y] <- System.Math.Max(arr.[x,y] - v, 0)
		arr

	let color (n:int) : ConsoleColor =
		match n with
		| x when x > 15 -> ConsoleColor.White
		| x when x < 0  -> ConsoleColor.Black
		| _             -> colorMap.[n]

	let draw (arr: int[,]) =
		let l = size arr
		for x in [0..l-1] do
			for y in [0..l-1] do
				let old = System.Console.ForegroundColor
				System.Console.ForegroundColor <- (color (arr.[x,y]))		
			    printf "%2s" (string(arr.[x,y]))
				System.Console.ForegroundColor <- old			
			printfn ""
		
		
	let analyze (arr: int [,]) (target:int) (pos:int) (neg:int) : int [,] =
		let l = size arr
		for x in [0..l-1] do
			for y in [0..l-1] do
				match (neighbors arr 1 1 |> List.toArray |> hasSubsetSum target) with
				| true  -> reward arr x y pos
				| false -> penalize arr x y neg
		arr

	let solution (t:int) (p:int) (n:int) = 
		let arr = board 30 80
		for _ in [0..100] do
			analyze arr t p n
			draw arr
			printfn ""
