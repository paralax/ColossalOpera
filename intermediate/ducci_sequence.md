# Title

The Ducci Sequence

# Difficulty

Intermediate

# Tags

number theory, sequence

# Description

A Ducci sequence is a sequence of n-tuples of integers, sometimes known as "the Diffy game", because it is based on sequences. Given an n-tuple of integers (a_1, a_2, ... a_n) the next n-tuple in the sequence is formed by taking the absolute differences of neighbouring integers. Ducci sequences are named after Enrico Ducci (1864-1940), the Italian mathematician credited with their discovery.

*Some* Ducci sequences descend to all zeroes or a repeating sequence. An example is (1,2,1,2,1,0) -> (1,1,1,1,1,1) -> (0,0,0,0,0,0). 

Additional information about the Ducci sequence can be found in [this writeup](http://www.cut-the-knot.org/Curriculum/Algebra/GregBrockman/GregBrockmanDucciSequences.shtml) from Greg Brockman, a mathematics student. 

It's kind of fun to play with the code once you get it working and to try and find sequences that never collapse and repeat. One I found was (2, 4126087, 4126085), it just goes on and on.

It's also kind of fun to plot these in 3 dimensions. [Here](https://monkey.org/~jose/graphing/ducci/index2.html) is an example of the sequence "(129,12,155,772,63,4)" turned into 2 sets of lines (x1, y1, z1, x2, y2, z2). 

# Input Description

You'll be given an *n*-tuple, one per line. Example:

    (0, 653, 1854, 4063)

# Output Description

Your program should emit the number of steps taken to get to either an all 0 tuple or when it enters a stable repeating pattern. Example:

    [0; 653; 1854; 4063]
    [653; 1201; 2209; 4063]
    [548; 1008; 1854; 3410]
    [460; 846; 1556; 2862]
    [386; 710; 1306; 2402]
    [324; 596; 1096; 2016]
    [272; 500; 920; 1692]
    [228; 420; 772; 1420]
    [192; 352; 648; 1192]
    [160; 296; 544; 1000]
    [136; 248; 456; 840]
    [112; 208; 384; 704]
    [96; 176; 320; 592]
    [80; 144; 272; 496]
    [64; 128; 224; 416]
    [64; 96; 192; 352]
    [32; 96; 160; 288]
    [64; 64; 128; 256]
    [0; 64; 128; 192]
    [64; 64; 64; 192]
    [0; 0; 128; 128]
    [0; 128; 0; 128]
    [128; 128; 128; 128]
    [0; 0; 0; 0]
    24 steps

# Challenge Input

    (1, 5, 7, 9, 9)
    (1, 2, 1, 2, 1, 0)
    (10, 12, 41, 62, 31, 50)
    (10, 12, 41, 62, 31)

# Fsharp solution

    let ducci (s:string) = 
        let x = Array.map int (s.Trim('(').Trim(')').Split(',')) |> List.ofArray
        let rec _ducci (a: int list) (seen: Set<int list>) = 
            printfn "%A" a
            match seen.Contains a with
            | true -> seen.Count-1
            | false -> let b = List.tail a @ [ List.head a] 
                               |> List.zip a 
                               |> List.map (fun (x,y) -> x-y) 
                               |> List.map (fun x -> System.Math.Abs(x))
                       _ducci b (Set.add a seen)
        let i = [ for _ in [0..(List.length x)] -> 0]
        _ducci x (Set.ofList [ i; i])
