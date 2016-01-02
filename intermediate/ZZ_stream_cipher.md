# Title

[2015-07-08] Challenge #222 [Intermediate] Simple Stream Cipher

# Difficulty

Intermediate

# Tags

random number, cipher, encryption, RC4

# Description

Stream ciphers like RC4 operate very simply: they have a strong psuedo-random number generator that takes a key and produces a sequence of psuedo-random bytes, which is then XORed against the plaintext to provide the cipher text. The strength of the cipher then depends on the strength of the generated stream of bytes - its randomness (or lack thereof) can lead to the text being recoverable.

# Challenge Description

Your program should have the following components:

* A psuedo-random number generator which takes a key and produces a consistent stream of psuedo-random bytes. A very simple one to implement is the [linear congruential generator (LCG)](https://en.wikipedia.org/wiki/Linear_congruential_generator )
* An "encrypt" function (or method) that takes a key and a plaintext and returns a ciphertext.
* A "decrypt" function (or method) that takes a key and the ciphertext and returns the plaintext. 

# Python Solution

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

# Scala Solution

    def lcg(m:Int, a:Int, c:Int, x:Int)=  (a*x + c) % m

    def enc(s:String, key:Int): List[Int] = 
        (0 to s.length).toList.foldLeft[List[Int]](List()){(acc, x) => if (acc.isEmpty) {List(lcg(128,664525, 1013904223,key))} else {lcg(128,664525, 1013904223,acc.head)::acc}}.zip(s.toCharArray).map(x => x._1^x._2)

    def dec(msg:List[Int], key:Int): String = 
        (0 to msg.length).toList.foldLeft[List[Int]](List()){(acc, x) => if (acc.isEmpty) {List(lcg(128,664525, 1013904223,key))} else {lcg(128,664525, 1013904223,acc.head)::acc}}.zip(msg).map(x => x._1^x._2).map(_.toChar).mkString
