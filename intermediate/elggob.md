# Title

Elgob - Make a Boggle Layout

# Difficulty

Intermediate

# Tags

word games, Boggle

# Description

The game of Boggle is familiar to many - a set of 36 6-sided dice with letters on them, which then turns into a 6x6 layout of letters, and then you work on finding properly spelled words by moving from one die to another. We've done a Boggle challenge in the past. In Boggle rules you may move left, right, up, down, and diagonally, but you may not use the same die twice as you spell a word. 

Now can you do it backwards? Given a list of target words, can you create a Boggle layout using any other letters you wish that could yield those words and more?

# Input Description

First you'll be given an integer on a line telling you how many words to target. Then you'll be given a list of *N* target words, one per line. Example:

    3 
    CATCHER
    MOUSE 
    AIRY 

# Output Description

Your program should emit a possible Boggle layout that could yield those words and any other ones that happen to be possible. For example:

    L   W   D   J   M   Q
    L   A	H	E	R   J
    K   C	I	E	S   O
    N   A	T	R	U   E
    P   C	Y	M	O   W
    T   E   O   H   T   C

Notice that you can spell words like COW, TOW, TOE, TOURS, and more in the above, in addition to the 3 words we had to target. 

# Challenge Input

    9
    MID
    RANA
    GRANT
    BOCCA
    CILIA
    WAIVE
    OSSAL
    SALMO
    FICE

# Credit

This challenge as inspired by [a question](https://www.reddit.com/r/compsci/comments/3zjt44/filling_a_grid_with_words_using_boggle_rules/) from /u/JRhapsodus. 