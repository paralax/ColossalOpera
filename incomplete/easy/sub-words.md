# Title

Sub-words

# Difficulty

Easy

# Description

We are interested in the unique words contained in a given string. Write a program that takes an input string and prints out all of its sub-words.

# Formal Input Description

Your program requires two inputs: a word and a word list.

* We define a word to be any string in the range [a-z].
* We define a word list to be a file where a word is on each line.

I suggest you use enable1.txt https://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt for your word list.

# Formal Output Description

We define a sub-word S to be a contiguous sequence of characters contained in a word W, where S is not W and where S is in the word list.
Consider the word "coat" — "at" and "oat" are sub-words because they:

* are contiguous characters found in "coat"
* are not "coat"
* are in enable1.txt https://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt

Note that "cat" is not a sub-word of "coat" because c, a, and t are not contiguous in "coat".

Your program must print all sub-words in the input word on a single line separated by commas. If a word has no sub-words, print "[word] has no sub-words."

# Sample Inputs

    ladder
    asidonwqe
    anteater
    apple

# Sample Outputs

    add, de, ad, la, adder, er, lad
    as, don, si, id, do, on
    tea, teat, ante, ate, at, ant, eater, eat, an, er
    apple has no sub-words.

Hints

Consider the word "banana" — a naive algorithm might produce duplicates, like this:

    ban, ba, ana, an, nana, nan, na, ana, an, na
    
We don't want duplicates:

    na, ana, nana, nan, an, ban, ba
    
# Bonus

In enable1.txt https://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt , find the word with the most sub-words and also the longest word without any sub-words.

# Notes

This challenge was suggested by user /u/chunes. If you have your own idea for a challenge, submit it to /r/DailyProgrammer_Ideas, and there's a good chance we'll post it.
