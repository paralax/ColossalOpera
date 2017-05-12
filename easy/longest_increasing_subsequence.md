# Title

Longest Increasing Subsequence

# Difficulty

Easy

# Tags

subsequence

# Description

In computer science, the longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique. 

In the first 16 terms of the binary Van der Corput sequence

    0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15

a longest increasing subsequence is

    0, 2, 6, 9, 11, 15.

This subsequence has length six; the input sequence has no seven-member increasing subsequences. 

Remember a subsequence needn't be made of contiguous elements from a sequence, you may remove intermediate sybmols but you may not move their relative positions. For example, if you have the sequence `a b c d`, a valid subsequence may be `a b d` having knocked out `c`. 

# Input Description

You'll be given a sequence of symbols (letters or integers) space separated, one sequence per line. Example:

	4 19 8 19 8 18 12 5 10 11 5

# Output Description

Your program should emit the length of the longest increasing subsequence. Optionally emit one of the examples. Example:

	3

# Challenge Input

	10 7 6 14 19 6 8 4 16 2 10
	3 11 13 4 0 7 15 7 7 2 15
	7 8 5 2 11 16 18 2 0 4 0

# Challenge Output

	5
	4
	5
