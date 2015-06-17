# Title

Simple Stream Cipher

# Difficulty

Intermediate

# Description

Stream ciphers like RC4 operate very simply: they have a strong psuedo-random number generator that takes a key and produces a sequence of psuedo-random bytes, which is then XORed against the plaintext to provide the cipher text. The strength of the cipher then depends on the strength of the generated stream of bytes - its randomness (or lack thereof) can lead to the text being recoverable.

# Challenge Description

Your program should have the following components:

* A psuedo-random number generator which takes a key and produces a consistent stream of psuedo-random bytes. A very simple one to implement is the linear congruential generator (LCG). https://en.wikipedia.org/wiki/Linear_congruential_generator 
* An "encrypt" function (or method) that takes a key and a plaintext and returns a ciphertext.
* A "decrypt" function (or method) that takes a key and the ciphertext and returns the plaintext. 

# Example in Python

    import sys
 
    # def xor(b, s): return "".join(map(lambda x: chr(x^b), map(lambda x: ord(x), s)))
    def xor(b, s): return map(lambda x: x^b, map(lambda x: ord(x), s))
 
    M = sys.maxsize
    M = 128
 
    def lcg(m, a, c, x): return (a*x + c) % m
 
    def enc(msg, seed):
        res = []
        for ch in msg:
            res.extend(xor(lcg(M, 1664525, 1013904223, seed), ch))
            seed = lcg(M, 1664525, 1013904223, seed)
        return res
 
    def dec(msg, seed):
        res = []
        for ch in msg:
            res.append(lcg(M, 1664525, 1013904223, seed)^ch)
            seed = lcg(M, 1664525, 1013904223, seed)
        return ''.join(map(chr, res))
