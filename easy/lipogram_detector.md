# Title

Lipogram Detector

# Difficulty

Easy

# Tags

word games, lipogram

# Description

A lipogram is a kind of constrained writing or word game consisting in writing paragraphs or longer works in which a particular letter or group of letters is avoided. Writing a lipogram may be a trivial task when avoiding uncommon letters like Z, J, Q, or X, but it is much more difficult to avoid common letters like E, T or A, as the author must omit many ordinary words. A famous example is Poe's poem *The Raven* contains no Z, but there is no evidence that this was intentional. Pangrammatic lipograms use all letters except one.

Your challenge today is to detect what letter is missing from the given text.

#  Input Description

You'll be given a short piece of text. For example:

    A jovial swain should not complain
    Of any buxom fair
    Who mocks his pain and thinks it gain
    To quiz his awkward air.

# Output Description

Your program should emit what letter is missing. From ths above example:

    E

# Challenge Input

    Bold Nassan quits his caravan,
    A hazy mountain grot to scan;
    Climbs jaggy rocks to find his way,
    Doth tax his sight, but far doth stray.

    Not work of man, nor sport of child
    Finds Nassan on this mazy wild;
    Lax grow his joints, limbs toil in vain-
    Poor wight! why didst thou quit that plain?

    Vainly for succour Nassan calls;
    Know, Zillah, that thy Nassan falls;
    But prowling wolf and fox may joy
    To quarry on thy Arab boy.

# Challenge Output

    E

# Scala Solution

    def lipogram(text: String) : Set[Char] = 
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toSet--text.toCharArray.map(_.toUpper).toSet

# Python Solution

    def lipogram(text): 
        return set(string.lowercase) - ( { ch.lower() for ch in text } - set(string.punctuation))
