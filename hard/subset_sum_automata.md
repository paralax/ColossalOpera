# Title

Subset Sum Automata

# Difficulty

Hard

# Tags

automata, subset sum

# Description

We recently did the [subset sum](https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/) problem wherein given a sequence of integers, can you find any subset that sums to 0. Today, inspired by [this post](https://thquinn.github.io/projects/automaton.html) let's play subset sum automata. It marries the subset sum problem with [Conway's Game of Life](https://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/). 

You begin with a board full of random integers in each cell. Cells will increment or decrement based on a simple application of the subset sum problem: if any subset of the 8 neighboring cells can sum to the target value, you increment the cell's sum by some value; if not, you decrement the cell by that value. Automata are defined with three integers `x/y/z`, where `x` is the target value, `y` is the reward value, and `z` is the penalty value. 
