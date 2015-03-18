# Title

Balancing Words

# Difficulty

Easy

# Description

Today we're going to balance words on one of the letters in them. We'll use the position and letter itself to calculate the weight around the balance point.

The formula to calculate the weight of the word is to look at the letter position in the English alphabet (so A=1, B=2, C=3 ... Z=26) as the letter weight, then multiply that by the distance from the balance point, so the first letter away is multiplied by 1, the second away by 2, etc. 

As an example:

STEAD balances at T: 1 * S(19) = 1 * E(5) + 2 * A(1) + 3 * D(4))

More info here: http://www.questrel.com/records.html#spelling_alphabetical_order_entire_word_balance_points

# Input Description

You'll be given a series of English words. Example:

    STEAD

# Output Description

Your program or function should emit the words split by their balance point. Example:

    S T EAD
    
This indicates that the T is the balance point.

# Challenge Input

    consubstantiation
    wrongheaded
    unintelligibility
    
# Credit

This was found on a word games page suggested by /u/cDull, thanks!

# Notes

If you have your own idea for a challenge, submit it to /r/DailyProgrammer_Ideas, and there's a good chance we'll post it.
