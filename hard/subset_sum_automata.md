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

	// generate board
	// iterate over each square finding NW,N,NE,E,SE,S,SW,W values 
	// apply subset sum to those values with target
	// increment or penalize the cell as needed
	// draw the board with color
	// Read and parse specification  
	// color print below


	// https://blogs.msdn.microsoft.com/chrsmith/2008/10/01/f-zen-colored-printf/
	let cprintf c fmt = 
	    Printf.kprintf
	        (fun s ->
	            let old = System.Console.ForegroundColor
	            try
	              System.Console.ForegroundColor <- c;
	              System.Console.Write s
	            finally
	              System.Console.ForegroundColor <- old)
	        fmt

	// Colored printfn
	let cprintfn c fmt =
	    cprintf c fmt
	    printfn ""

	open System

	cprintfn ConsoleColor.Blue  "Hello, World in BLUE!"
	cprintfn ConsoleColor.Red   "… and in RED!"
	cprintfn ConsoleColor.Green "… and in GREEN!"

	let rotatingColors =
	    seq {
	        let i = ref 0
	        let possibleColors = Enum.GetValues(typeof<ConsoleColor>)
	        while true do
	            yield (enum (!i) : ConsoleColor)
	            i := (!i + 1) % possibleColors.Length
	    }

	"Experience the rainbow of possibility!"
	|> Seq.zip rotatingColors
	|> Seq.iter (fun (color, letter) -> cprintf color "%c" letter)
