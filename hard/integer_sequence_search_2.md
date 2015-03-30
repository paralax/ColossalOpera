# Title

Integer Sequence Search Part 2

# Difficulty

Hard

# Description

This is part 2 of the Integer sequence search functionality. An integer sequence is a sequence (i.e., an ordered list) of integers. 

Not all sequences are computable (e.g. not all have a formula that can express them), but many do. 

For this challenge you'll be searching sequences expressed as a recurrence relation.

# Input Description

You'll be given two integers, *N* and *M*, which tell you how many sequences to read to form your database and then how many search queries to process, respectively. Then you'll be given the database as *N* pairs of *name* and *recurrence relation* pair. Then you'll be given *M* queries of a series of integers. Not all sequences you will be searching for will start at the beginning. Note that the overlap of the query and the sequence database will be unambiguous but is not guaranteed to overlap completely. Sequence names will use the OEIS naming convention.

Recurrence relations will be given as a relationship of numbers in the sequence and the starting conditions.

Example:

	1 1
	A000045 F(n) = F(n-1)+F(n-2) with F(0)=0, F(1)=1
	0, 1, 1, 2, 3, 5, 8, 13 

# Output Description

Your program should emit the sequence and its OEIS identifier. Use the identifier "NOTFOUND" for those not in the database. Example:

	0, 1, 1, 2, 3, 5, 8, 13 A000045

# Challenge Input

	5 6
	A000045 F(n) = F(n-1)+F(n-2) with F(0)=0, F(1)=1
	A000931	F(n) = F(n-2)+F(n-3) with F(0)=1, F(1)=0, F(2)=0
	A001608	F(n) = F(n-2)+F(n-3) with F(0)=3, F(1)=0, F(2)=2
	A000032	F(n) = F(n-1)+F(n-2)
	A001608	F(n) = F(n-2)+F(n-3) with F(0)=3, F(1)=0, F(2)=2
	0, 1, 1, 2, 3, 5, 8, 13 A000045	
	1, 0, 1, 1, 1, 2, 2, 3, 4, 5 
	3, 0, 2, 3, 2, 5, 5, 7, 10, 12 
	2, 1, 3, 4, 7, 11, 18, 29, 47, 76 
	3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17 	
	1, 1, 5, 5, 45, 95, 465, 1165 

# Challenge Output

	1, 0, 1, 1, 1, 2, 2, 3, 4, 5 A000931
	3, 0, 2, 3, 2, 5, 5, 7, 10, 12 A001608
	2, 1, 3, 4, 7, 11, 18, 29, 47. 76 A000032
	3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17 A001608	
	1, 1, 5, 5, 45, 95, 465, 1165 NOTFOUND
