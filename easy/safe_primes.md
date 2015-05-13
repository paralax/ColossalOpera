# Title 

Safe Prime Numbers 

# Difficulty 

Easy

# Description

A safe prime is a prime number of the form 2*p* + 1, where p is also a prime. Safe primes are also important in cryptography because of their use in discrete logarithm-based techniques like Diffie-Hellman key exchange.

#  Input Description

You will be given a single number that is the maximum value of safe prime to search for. Example: 

	100

# Output Description 

A list of numbers, one on each line, showing numbers that solve the safe prime definition. Example:

	5
	7
	11
	23
	47
	59
	83

# Challenge Input

	1000

# Challenge Input Solution (not visible by default)

	5
	7
	11
	23
	47
	59
	83
	107
	167
	179
	227
	263
	347
	359
	383
	467
	479
	503
	563
	587
	719
	839
	863
	887
	983



# FSharp solution

	> let isprime (n:int) =                                                             
	-     let n = bigint(n)
	-     let rec check i =
	-         i > n/2I || (n % i <> 0I && check (i + 1I))
	-     check 2I
	-- ;;


	> let safeprimes(n:int) =
	-     [ 2..n ] |> List.filter (fun x ->isprime(x) && isprime(1+2*x) )
	- ;;

	val safeprimes : n:int -> int list

	> safeprimes 100 ;;
	val it : int list = [2; 3; 5; 11; 23; 29; 41; 53; 83; 89]
	> safeprimes 1000 ;;
	val it : int list =
	  [2; 3; 5; 11; 23; 29; 41; 53; 83; 89; 113; 131; 173; 179; 191; 233; 239; 251;
	   281; 293; 359; 419; 431; 443; 491; 509; 593; 641; 653; 659; 683; 719; 743;
	   761; 809; 911; 953]
