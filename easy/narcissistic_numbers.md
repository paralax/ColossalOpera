# Title

Narcissistic numbers

# Difficulty

Easy

# Tags

number theory

# Description

In recreational number theory, a narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits. These numbers are also known as a pluperfect digital invariant (PPDI), or Armstrong numbers (after Michael F. Armstrong). 

For example the 3-digit decimal number 153 is a narcissistic number because 153 = 1^3 + 5^3 + 3^3.

You can also express narcissistic numbers in bases other than base 10. 

Clearly, in all bases, all one-digit numbers are narcissistic numbers (e.g. 5 = 5^1). The sequence of base 10 narcissistic numbers starts: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407 ... 

# Input Description

You'll be given a number, one per line. Example:

	370
	372

# Output Description

Your program should emit if the number is narcissistic or not. Example:

	370 NARCISSISTIC 370 = 3^3 + 7^3 + 0^3
	372 NOT NARCISSISTIC

# Challenge Input

	22
	371
	978
	1634
	2874
	9474

# Challenge Output

	22 NOT NARCISSISTIC
	371 NARCISSISTIC 371=3^3 + 7^3 + 1^3
	978 NOT NARCISSISTIC
	1634 NARCISSISTIC 1634=1^4 + 6^4 + 3^4 + 4^4
	2874 NOT NARCISSISTIC
	9474 NARCISSISTIC 9474=9^4 + 4^4 + 7^4 + 4^4

# FSharp Solution

	let narcissistic(n:int) : string = 
		let s = string n
		let m = s.ToCharArray()
				|> Array.map (fun x -> int(string x)) 
				|> Array.map (fun x -> System.Math.Pow(float x, float (s.Length)))
				|> Array.sum 
				|> int
		let format(s:string) : string =
			let a = s.ToCharArray()
					|> Array.map string
					|> Array.map (fun x -> System.String.Format("{0}^{1}", x, s.Length))
			"NARCISSISTIC " + s + "=" + System.String.Join(" + ", a)
		match n = m with
		| true  -> format s
		| false -> "NOT NARCISSISTIC"
