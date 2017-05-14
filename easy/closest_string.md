# Title

Closest String

# Difficulty

Easy

# Tags

string, string distance

# Description

In theoretical computer science, the closest string is an NP-hard computational problem, which tries to find the geometrical center of a set of input strings. To understand the word "center", it is necessary to define a distance between two strings. Usually, this problem is studied with the Hamming distance in mind. This center must be one of the input strings.

In bioinformatics, the closest string problem is an intensively studied facet of the problem of finding signals in DNA. In keeping with the bioinformatics utility, let's consider DNA sequences. 

Consider the following DNA sequences:

    ATCAATATCAA
    ATTAAATAACT
    AATCCTTAAAC
    CTACTTTCTTT
    TCCCATCCTTT
    ACTTCAATATA

Using the Hamming distance (the number of different characters bewteen two sequences of the same length), the all-pairs distances of the above 6 sequences puts `ATTAAATAACT` at the center. 

# Input Description

You'll be given input with the first line an integer *N* telling you how many lines to read for the input, then that number of lines of strings. All strings will be the same length. Example:

    4
    CTCCATCACAC
    AATATCTACAT
    ACATTCTCCAT
    CCTCCCCACTC

# Output Description

Your program should emit the string from the input that's closest to all of them. Example:

    ACATTCTCCAT
    
# Challenge Input

    10
    AACACCCTATA
    CTTCATCCACA
    TTTCAATTTTC
    ACAATCAAACC
    ATTCTACAACT
    ATTCCTTATTC
    ACTTCTCTATT
    TAAAACTCACC
    CTTTTCCCACC
    ACCTTTTCTCA
    TACCACTACTT
    
    20
    ACAAAATCCTATCAAAAACTACCATACCAAT
    ACTATACTTCTAATATCATTCATTACACTTT
    TTAACTCCCATTATATATTATTAATTTACCC
    CCAACATACTAAACTTATTTTTTAACTACCA
    TTCTAAACATTACTCCTACACCTACATACCT
    ATCATCAATTACCTAATAATTCCCAATTTAT
    TCCCTAATCATACCATTTTACACTCAAAAAC
    AATTCAAACTTTACACACCCCTCTCATCATC
    CTCCATCTTATCATATAATAAACCAAATTTA
    AAAAATCCATCATTTTTTAATTCCATTCCTT
    CCACTCCAAACACAAAATTATTACAATAACA
    ATATTTACTCACACAAACAATTACCATCACA
    TTCAAATACAAATCTCAAAATCACCTTATTT
    TCCTTTAACAACTTCCCTTATCTATCTATTC
    CATCCATCCCAAAACTCTCACACATAACAAC
    ATTACTTATACAAAATAACTACTCCCCAATA
    TATATTTTAACCACTTACCAAAATCTCTACT
    TCTTTTATATCCATAAATCCAACAACTCCTA
    CTCTCAAACATATATTTCTATAACTCTTATC
    ACAAATAATAAAACATCCATTTCATTCATAA
    CACCACCAAACCTTATAATCCCCAACCACAC

# Challenge Output

    ATTAAATAACT
    
    TTAACTCCCATTATATATTATTAATTTACCC

# Bonus

All-pairs distances is great until you wind up with a lot of inputs. Can you come up with a more efficient solution? 

# FSharp Solution

This is a naive all-pairs distances approach, with O(N^2) complexity.

    let hamming (a:string) (b:string) : int =
        Array.zip (a.ToCharArray()) (b.ToCharArray()) |> Array.filter (fun (x,y) -> x <> y) |> Array.length
    let distances (xs:string list) : Map<string, int list> = 
        let mapget (m:Map<string, int list>) (key:string) : int list =
            match (Map.tryFind key m) with
            | Some(x) -> x
            | None    -> []
        let rec loop (a:string) (bs:string list) (m:Map<string, int list>): Map<string, int list> =
            match bs with
            | [] -> m
            | _  -> let d = hamming a (List.head bs)
                    let ds = mapget m a            
                    loop a (List.tail bs) (Map.add a (d::ds) m)
        List.fold (fun acc x -> loop x xs acc) Map.empty xs
    let solution (seqs:string []) : string * int = 
        distances (List.ofArray seqs) 
        |> Map.map (fun k v -> (k,(List.sum v))) 
        |> Map.toList 
        |> List.map snd 
        |> List.minBy snd  
