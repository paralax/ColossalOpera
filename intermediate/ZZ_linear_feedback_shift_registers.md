# Title

[2018-01-17] Challenge #347 [Intermediate] Linear Feedback Shift Register

# Difficulty

Intermediate

# Tags

binary arithmetic, random numbers, digital registers

# Description

In computing, a [linear-feedback shift register (LFSR)](https://en.wikipedia.org/wiki/Linear-feedback_shift_register) is a shift register whose input bit is a linear function of its previous state. The most commonly used linear function of single bits is exclusive-or (XOR). Thus, an LFSR is most often a shift register whose input bit is driven by the XOR of some bits of the overall shift register value.

The initial value of the LFSR is called the seed, and because the operation of the register is deterministic, the stream of values produced by the register is completely determined by its current (or previous) state. Likewise, because the register has a finite number of possible states, it must eventually enter a repeating cycle.

Your challenge today is to implement an LFSR in software. 

# Example Input

You'll be given a LFSR input on one line specifying the tap positions (0-indexed), the feedback function (XOR or [XNOR](https://en.wikipedia.org/wiki/XNOR_gate)), the initial value with leading 0s as needed to show you the bit width, and the number of clock steps to output. Example:

    [0,2] XOR 001 7

# Example Output

Your program should emit the clock step and the registers (with leading 0s) for the input LFSR. From our above example:

    0 001
    1 100
    2 110 
    3 111
    4 011
    5 101
    6 010
    7 001

# Challenge Input

    [1,2] XOR 001 7
    [0,2] XNOR 001 7
    [1,2,3,7] XOR 00000001 16
    [1,5,6,31] XOR 00000000000000000000000000000001 16

# Challenge Output

(Only showing the first two for brevity's sake.)

    0 001
    1 100 
    2 010
    3 101
    4 110
    5 111
    6 011
    7 001

----

    0 001
    1 000
    2 100
    3 010
    4 101
    5 110
    6 011
    7 001 

# Further Reading

- [Tutorial: Linear Feedback Shift Registers (LFSRs) - Part 1](https://www.eetimes.com/document.asp?doc_id=1274550) from the IEEE
- [Linear Feedback Shift Registers Theory and Applications](http://homepages.cae.wisc.edu/~ece553/handouts/LFSR-notes.PDF) - some lecture notes from Kwal Saluja

# Bonus

Write a function that detects the periodicity of the LFSR configuration. 
