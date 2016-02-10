# Title

Calculating Shannon Entropy of a String

# Difficulty

Easy

# Tags

Shannon entropy

# Description

Shannon entropy was introduced by Claude E. Shannon in his 1948 paper "A Mathematical Theory of Communication". Somewhat related to the physical and chemical concept entropy, the Shannon entropy measures the uncertainty associated with a random variable, i.e. the expected value of the information in the message (in classical informatics it is measured in bits). This is a key concept in information theory and has consequences for things like compression, cryptography and privacy, and more. 

The Shannon entropy *H* is calculated as -1 times the sum of the frequency of the symbol times the log base 2 of the frequency:

                n
                _   count(i)          count(i)
    H(X) = -1 * >   --------- * log  (--------)
                -       N          2      N
                i=1

For more, see Wikipedia for [Entropy in information theory](https://en.wikipedia.org/wiki/Entropy_(information_theory)). 

# Input Description

You'll be given a string, one per line, for which you should calculate the Shannon entropy. Examples:

    1223334444
    Hello, world!

# Output Description

Your program should emit the calculated entropy values for the strings to at least five decimal places. Examples:

    1.84644
    3.18083

# Challenge Input

    122333444455555666666777777788888888
    563881467447538846567288767728553786
    https://www.reddit.com/r/dailyprogrammer
    int main(int argc, char *argv[])

# Challenge Output

    2.794208683
    2.794208683
    4.056198332
    3.866729296

# Python Solution

    import math

    from collections import Counter

    def entropy(s):
        p, lns = Counter(s), float(len(s))
        return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

# FSharp Solution

    let entropy (s) : float = 
        let p = string(s).ToCharArray() 
                |> Seq.groupBy (fun x -> x) 
                |> Seq.map (fun (x,y) -> Seq.length y)
        -1.0 * ([ for count in p -> 
                    float(count)/float(String.length(s)) *
                    System.Math.Log(float(count)/float(String.length(s)), 2.0) ] 
                |> Seq.sum )
