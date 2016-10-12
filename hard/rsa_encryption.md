# Title

Implement Basic RSA Public Key Encryption

# Difficulty

Hard

# Tags

encryption, cipher, RSA, public-key encryption

# Description

For today's challenge we'll implement a basic version of the RSA public key algorithm. Public key encryption algorithms allow for one to share a *public* key which enables people to generate a message that only the *private* key (which you hold secret) can decrypt. The mathematics rely on the challenge of factoring the product of two large primes. 

To generate an RSA key pair (the functions *gcd* and *phi* are described below):

- Select *p*, *q* such that *p* and *q* are both prime and *p != q* (they need to be distinct)
- Calculate *n = p\*q* 
- Calculate *phi(n) = (p-1)(q-1)* 
- Select an integer *e* such that *gcd(phi(n), e) = 1; 1 < e < phi(n)*
- Calculate *d* such that *d = e^(-1)mod phi(n)* 
- The public key KU = *{e, n}*
- The private key KR = *{d, n}* 

The Euler totient function *phi* for a value *n* is the number of positive integers less than *n* that are prime relative to *n*. For example, *phi(37)* is 36 - there are 36 numbers up to 37 that are relatively prime. However, *phi(35)* is 24 - there are only 24 numbers up to 35 that are relatively prime (e.g. 5 divides both 5 and 35, so we can't count that one). Interestingly enough for a prime number *p* the value of *phi(p)* is *p - 1*. 

The greatest common divisor *gcd()* is the greatest common divisor for two numbers *a* and *b* - what number divides both *a* and *b* properly, no remainders.

To encrypt a value M (e.g. a two digit number), we calculate *M^e mod n* which yields us an encrypted value *E*; to decrypt we calculate *E^d mod n*, which yields our plaintext value *M*. 

For this challenge we'll generate some super weak keys - we'll use small prime numbers to avoid getting into arbitrary precision math, but you're free to make them as big as you wish. 

# Example

- We select two prime numbers, p = 17 and q = 11
- We calculate n = pq = 17 \* 11 = 187
- We calculate *phi(n) = (p-1)(q-1) = 16 * 10 = 160*
- We select *e* that is relatively prime to *phi(n) = 160* and less than *phi(n)* - we come up with *e = 7*
- We determine *d* such that *de = 1 mod 160* and *d < 160*. This leaves us with *d = 23* because *23 \* 7 = 161 = 10 \* 160 + 1*

This leaves us with *KU = {7, 187}* and *KR = {23, 187}*. 

Now to encrypt a simple message of *M = 88*. To encrypt we have to calculate *88^7 mod 187* which yields 11, which we transmit. The receiver decrypts by calculating *11^(23) mod 187* which yields 88, our original message. 
