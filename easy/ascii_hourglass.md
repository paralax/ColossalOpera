# Title

Hourglass Maker

# Difficulty

Easy

# Description

Creating ASCII art can be fun, especially if it's based on a rule. For this challenge you'll be making ASCII hourglasses. A simple output would use asterisks. 

The input will be an integer, and your output should emit that many rows balanced as an hourglass. An example output for the number 9 would be:

	* * * * *
	 *     *
	  *   *
	   * *
	    *
	   * *
	  *   *
	 *     *
	* * * * *
	
An alternative output emits numbers:

	9 7 5 3 1
	 8     2
	  7   3
	   6 2
	    5
	   6 2
	  7   3
	 8     2
	9 7 5 3 1

The rule is quite simple:

	n n-2 n-4 ... 1
	 n-1         2
	  n-2       3
	   ...
	     ceil(n/2)
	   ...

# Inputs

	5
	8
	
# Outputs

	5 3 1
	 4 2 
	  3  
	 4 2 
	5 3 1

	8 6  3 1
	 7    2 
	  6  3  
	   54   
	   54   
	  6  3  
	 7    2 
	8 6  3 1

# Notes

Many thanks to Redditor /u/tajjet for this submission to /r/dailyprogrammer_ideas. If you have any ideas, please submit them there!
