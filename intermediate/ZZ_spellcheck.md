# Title

[2015-09-30] Challenge #234 [Intermediate] Red Squiggles

# Difficulty

Intermediate

It looks like the moderators fell down on the job! I'll send in an emergency challenge. 

# Description

Many of us are familiar with real-time spell checkers in our text editors. Two of the more popular editors Microsoft Word or Google Docs will insert a red squiggly line under a word as it's typed incorrectly to indicate you have a problem. (Back in my day you had to run spell check *after* the fact, and that was an extra feature you paid for. Real time was just a dream.) The lookup in a dictionary is dynamic. At some point, the error occurs and the number of possible words that it could be goes to zero. 

For example, take the word `foobar`. Up until `foo` it could be words like `foot`, `fool`, `food`, etc. But once I type the `b` it's appearant that no words could possibly match, and Word throws a red squiggly line. 

Your challenge today is to implement a real time spell checker and indicate where you would throw the red squiggle. For your dictionary use `/usr/share/dict/words` or the always useful `enable1.txt`. 

# Input Description

You'll be given words, one per line. Examples:

    foobar
    garbgae

# Output Description

Your program should emit an indicator for where you would flag the word as mispelled. Examples:

    foob<ar
    garbg<ae

Here the `<` indicates "This is the start of the mispelling". If the word is spelled correctly, indicate so.

# Challenge Input

    accomodate
    acknowlegement
    arguemint 
    comitmment 
    deductabel
    depindant
    existanse
    forworde
    herrass
    inadvartent
    judgemant 
    ocurrance
    parogative
    suparseed

# Challenge Output

    accomo<date
    acknowleg<ement
    arguem<int
    comitm<ment
    deducta<bel
    depin<dant
    existan<se
    forworde<
    herra<ss
    inadva<rtent
    judgem<ant
    ocur<rance
    parog<ative
    supars<eed

# Bonus

Include some suggested replacement words using any strategy you wish (edit distance, for example, or where you are in your data structure if you're using a trie). 

# Scala Solution

    def spellcheck(word:String):String = {
        def loop(word:String, sofar:Int, matches:List[String]): String = {
            if ((word.length == sofar) && (matches.contains(word))) {return word + " is spelled correctly"}
            matches match {
                case Nil => word.slice(0, sofar-1) + "<" + word.slice(sofar-1, word.length)
                case _   => loop(word, sofar+1, matches.filter(_.startsWith(word.slice(0, sofar))))
            }
        }
        loop(word, 1, scala.io.Source.fromFile("/usr/share/dict/words").getLines.toList.filter(_.startsWith(word.slice(0, 1))))
    }
