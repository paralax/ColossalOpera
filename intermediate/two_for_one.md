# Title

Two for One

# Difficulty

Intermediate

# Tags

words, word play

# Description

This game is simple - swap one letter in the input word with a new pair of two letters (e.g. p -&gt; nn) to generate a valid resulting word (English words, only, please). 

# Formal Input Description

You'll be given a list of English words as input.

# Formal Output Description

Your program should emit the valid English words that result from the substitution. Use the [enable wordlist](https://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt) if you lack a list of English words (e.g. /usr/share/dict/words).

# Sample Input

    chapel
    agenda

# Sample Output

    channel
    addenda

# Challenge Input

    barber
    cogent
    staple
    behave
    axle

# Challenge Input Solution (not visible by default)

    barbell
    comment
    steeple
    behoove
    apple

# Note (optional)

This was from the NYTimes magazine on March 16. Puzzle credit goes to the always estimable Will Shortz. 

Have a cool idea for a challenge? Submit it to /r/DailyProgrammer_Ideas!

# Scala Solution

    def candidates(word:String): List[String] = {
        val len = word.length
        scala.io.Source.
                      fromFile("/usr/share/dict/words").
                      getLines.
                      filter(_.length == len+1).
                      toList
    }

    def hammingDistance(a:String, b:String): Int = 
        a.toCharArray.zip(b.toCharArray).filter(x => (x._2 != x._1)).length

    def twoforone(a:String, b:String): Boolean = {
        for (i <- (0 to a.length-1)) {
            if (a(i) != b(i)) {
                println((a.slice(0,i) + b(i) + b(i) + a.slice(i+1, a.length)))
                if (a.slice(0,i) + b(i) + b(i) + a.slice(i+1, a.length) == b) {
                    return true
                }
            }
        } 
        return false
    }

    def check(word:String): List[String] = 
        candidates(word).filter(x => hammingDistance(word, x) == 3).filter(x => twoforone(word, x))


