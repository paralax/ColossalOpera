# Title

Spoonerism

# Difficulty

Intermediate

# Tags

words, word play

# Description

A spoonerism is an error in speech or deliberate play on words in which corresponding consonants, vowels, or morphemes are switched (see metathesis) between two words in a phrase. It is named after the Reverend William Archibald Spooner (1844–1930), Warden of New College, Oxford, who was notoriously prone to this mistake. The term "Spoonerism" was well established by 1921. 

Example spoonerisms include:

* "A blushing crow." ("crushing blow")
* "Resident Pagan" (President Reagan)
* "belly jeans" (jelly beans)

Generating spoonerisms is kind of tricky, but follows a simple rule: swap the leading consonants of the two words. Programmatically this is easy, adjusting spelling for the pronunciation is tougher (and out of scope for this challenge). 

# Input Description

You'll be given a two word phrase, one per line, for which to generate a spoonerism. Words with which you need to swap letters will be capitalized to differentiate from stop words. Example:

    Bold Clue

# Output Description

Your program should emit the spoonerism form of the two word phrase. Spelling isn't an issue. Example:

    Bold Clue -> Cold Blue

# Challenge Input

    Swap Letters
    Lord of the Flies
    Daily Bread

# Challenge Output

    Swap Letters -> Lap Swetters (which sounds like "Lop Sweaters")
    Lord of the Flies -> Flord of the Lies (which is awfully close to "Ford of the Lies")
    Daily Bread -> Braily Dead (or "Baily Dread")
