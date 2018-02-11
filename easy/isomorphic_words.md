# Title

Isomorphic Words

# Difficulty

Easy

# Tags

word play

# Description

In graph theory, geometry and other mathematical subjects, an isomorph can be thought of as a relationship between two inputs that share a similar structure. We'll define the relationship between two words as being *isomorphic* if they reuse letters in the same pattern. As an example, the words `ESTATE` and `DUELED` both have the pattern `abcdca`:

    ESTATE
    DUELED
    abcdca

Put another way, you can deduce a simple substitution cipher to convert from one word to another. 

# Input Description

Write code that takes two words and checks whether they are isomorphic. You'll be given two words per line and asked to determine if they're isomorphic to one another. Example:

    ESTATE DUELED
    FEED DEAD

# Output Description

Your program should emit if the two words are isomorphic or not. Example:

    ESTATE DUELED TRUE
    FEED DEAD FALSE

# Challenge Input

    RAMBUNCTIOUSLY THERMODYNAMICS
    DISCRIMINATIVE SIMPLIFICATION
    BANANA SENSES
    SNACK HEATER

# Challenge Output

    RAMBUNCTIOUSLY THERMODYNAMICS TRUE
    DISCRIMINATIVE SIMPLIFICATION TRUE
    BANANA SENSES FALSE
    SNACK HEATER FALSE

# Scala Solution

    def isomorphic(w1:String, w2:String): Boolean = {
        val m = w1.zip(w2).toMap
        w2 == w1.map(x => m(x)).mkString
    }

# FSharp Solution

    let isomorphic (w1:string) (w2:string): bool = 
        let m = Array.zip (w1.ToCharArray()) (w2.ToCharArray()) |> Map.ofArray
        w2 = (Array.map (fun x -> string(Map.find x m)) (w1.ToCharArray()) |> String.concat "")
