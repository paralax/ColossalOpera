# Title

[2017-06-12] Challenge #319 [Easy] Condensing Sentences

# Difficulty

Easy

# Tags

word games, word play

# Description

Compression makes use of the fact that repeated structures are redundant, and it's more efficient to represent the pattern and the count or a reference to it. Similarly, we can *condense* a sentence by using the redundancy of overlapping letters from the end of one word and the start of the next. In this manner we can reduce the size of the sentence, even if we start to lose meaning. 

For instance, the phrase "live verses" can be condensed to "liverses". 

In this challenge you'll be asked to write a tool to condense sentences.

# Input Description

You'll be given a sentence, one per line, to condense. Condense where you can, but know that you can't condense everywhere. Example:

    I heard the pastor sing live verses easily.

# Output Description

Your program should emit a sentence with the appropriate parts condensed away. Our example:

    I heard the pastor sing liverses easily. 

# Challenge Input

    Deep episodes of Deep Space Nine came on the television only after the news.
    Digital alarm clocks scare area children.

# Challenge Output

    Deepisodes of Deep Space Nine came on the televisionly after the news.
    Digitalarm clockscarea children.
