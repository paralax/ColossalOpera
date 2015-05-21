# Title

Cyclic Words

# Difficulty

Intermediate

# Description

A cyclic word is a word that can be cleaved somewhere in the middle of it, the two halves swapped and then rejoined to form another legitimate word. For example the word `slaughter` is one with `laughters` - cleave after the `s` and move `laughter` from the end to the beginning.

For this challenge you can use the famous `enable1.txt` file or `/usr/share/dict/words`, as long as it's an English dictionary. 

# Input Description

You'll be given an integer on one line telling you how many words to read, then a list of *N* words words to read. Example:

    2
    slaughter
    calculate

# Output Description

Your program should emit if the words are cyclic in some fashion. Example:

    slaughter CYCLIC
    calculate NOT CYCLIC

# Challenge Input

    10
    large
    easel
    steak
    believe
    spot
    words 
    overt
    respite
    ranger
    neurectomy

# Challenge Output

    large NOT CYCLIC
    easel CYCLIC
    steak CYCLIC
    believe NOT CYCLIC
    spot CYCLIC
    words CYCLIC
    overt NOT CYCLIC
    respite NOT CYCLIC
    ranger NOT CYCLIC
    neurectomy NOT CYCLIC
