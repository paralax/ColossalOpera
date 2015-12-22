# Title

Integer Sequence Search Part 1

# Difficulty

Easy

# Tags

integer sequence, math

# Description

In mathematics, an integer sequence is a sequence (i.e., an ordered list) of integers. Not all sequences are computable (e.g. not all have a formula that can express them), but unique sequences have interesting properties and can be quite fun to watch play out. 

The [On-Line Encyclopedia of Integer Sequences (OEIS)](https://oeis.org/) website has an interesting feature where you can search for sequences by name, ID, or even just subsequences. 

For this challenge you'll be replicating that subsequence search feature. 

# Input Description

You'll be given two integers, *N* and *M*, which tell you how many sequences to read to form your database and then how many search queries to process, respectively. Then you'll be given the database as *N* pairs of *name* and *first 10 terms of the sequence* pair. Then you'll be given *M* queries of a series of integers. Note that the overlap of the query and the sequence database will be unambiguous but is not guaranteed to overlap completely. All sequences to search will be contiguous (e.g. no gaps). Sequence names will use the OEIS naming convention

Example:

	1 2
	A000055	1, 1, 1, 1, 2, 3, 6, 11, 23, 47
	11, 23, 47, 106
	3, 14, 15, 92, 65

# Output Description

For each of the search terms you should emit the query and the sequence name. 

Example:

	11, 23, 47, 106   A000055
	3, 14, 15, 92, 65 NOMATCH

# Challenge Input

	9 6
	A000055	1, 1, 1, 1, 2, 3, 6, 11, 23, 47
	A000045	0, 1, 1, 2, 3, 5, 8, 13, 21, 34
	A050278	1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987, 1023457689, 1023457698, 1023457869, 1023457896
	A000010	1, 1, 2, 2, 4, 2, 6, 4, 6, 4
	A194508	-1, 1, 0, 2, 1, 0, 2, 1, 3, 2
	A000111	1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936
	A233586	1, 6, 12, 19, 63, 263, 856, 2632, 7714, 9683
	A000391	1, 6, 21, 71, 216, 672, 1982, 5817, 16582, 46633
	A000713	1, 3, 8, 18, 38, 74, 139, 249, 434, 734
	1, 3, 8, 18
	263, 856, 2632, 7714, 9683
	1, 1, 2, 3, 5, 8
	1, 6, 12, 19, 63
	20, 22, 24, 28, 30, 34
	434, 734, 1215, 1967, 3132, 4902

# Challenge Output

	1, 3, 8, 18		A000713
	263, 856, 2632, 7714, 9683 	A233586
	1, 1, 2, 3, 5, 8	A000045
	1, 6, 12, 19, 63	A233586
	20, 22, 24, 28, 30, 34	NOMATCH
	434, 734, 1215, 1967, 3132, 4902 A000713