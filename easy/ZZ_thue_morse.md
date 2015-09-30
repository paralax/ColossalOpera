# Title

Thue-Morse Sequence Generator

# Description

The Thue-Morse sequence is a binary sequence (of 0s and 1s) that never repeats. 
It is obtained by starting with 0 and successively calculating the Boolean complement 
of the sequence so far. It turns out that doing this yields an infinite, 
non-repeating sequence. This procedure yields 0 then 01, 0110, 01101001, 
0110100110010110, and so on. 

See the [Thue-Morse Wikipedia Article](http://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence) for more information.


# Input
Nothing.

# Output
Output the 0 to 6th order Thue-Morse Sequences.

## Example

    nth         Sequence
    ===========================================================================
    0           0
    1           01
    2           0110
    3           01101001
    4           0110100110010110
    5           01101001100101101001011001101001
    6           0110100110010110100101100110100110010110011010010110100110010110

# Extra Challenge

Be able to output any nth order sequence. Display the Thue-Morse Sequences for 100.

Note: Due to the size of the sequence it seems people are crashing beyond 25th order or the time it takes is very long. So how long until you crash. Experiment with it.

# Fsharp Solution

    let rec A3061 (L) =
        match (List.head L, List.tail L) with
        | (1, []) -> [ 0 ]
        | (0, []) -> [ 1 ]
        | (1, _ ) -> [ 0 ] @ A3061 (List.tail L)
        | (0, _ ) -> [ 1 ] @ A3061 (List.tail L)

    let thuemorse (n:int) = 
        let mutable L = [0]
        for i in [1..n] do
            L <- L @ A3061 L
        L