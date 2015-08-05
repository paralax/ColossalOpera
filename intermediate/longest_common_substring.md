# Title

Needles in Haystacks

# Difficulty

Intermediate

# Description

Most of us are familiar with the concept of subsequences - a short string contained in a larger string is just a sequence of characters. It has a role in things like Markov models, suffix trees, and biological sequence motif analysis. 

For this challenge, your job is to implement a means to find the longest common substring between two strings. In this particular challenge data set I chose strings I built using a simple password generator based on English-language syllables. 

# Sample Input

You'll be given an integer on a line telling you how many pairs of words to read. Then you'll get that many lines of two words apiece. Example:

    1
    ARORHEREVESTNGEVEATALLULD HEANTOORISINOMETIOARNE

# Sample Output

Your program should emit the longest common substring between the two strings. Example:

    AR

# Challenge Input

    6
    ARTHAOURENESERAHENNDTHER OMEWITHEVEROMENOTHERERETHIFOR
    REENTHISHEERVERANDINGERATHE NTBUTTIOSHOSHONDMEULDTHIWIT
    HESHOMEMEULDSEINVERNTVER WITSEEREVEEREWASWAESARERE
    ARENEOMEINGERSTAROULHIITH ERTIOVERBUTOULVERVETHIWAER
    ESYOUORTHAREFORHEOULLEVER HENNTMEVERHERBUTISHISHANT
    VERNTMETERARHADHIFORERAENIONNGULDMEOMEHERTHTERERORNOTHAANLEONTHIHATSTANDERTHETHALEREHEOURTETIOALITHLEEREEVEATHINHISSHOHATNGULDENTTHAASSEALLHINITHSEARETINEESTEWAWATEDVEHIEAVEEDEAONNDTHAERAALLWITTIITTOINGFOROUREBUTIONASTEDNOTISOULOMEENTTHENTARESWASHER ENTHADESANTEERWITOULHEVEEAHERTHARETIBUTNOTTHAAREANDARAREOMEHIENOULALNTINGTIOITHWITTIOVERTERHATHALLEVEITHISONALEAERSELEULDNOTORHINANHINTEDASYOULEHATTHITOWASENTERASHOARTEDNGISSEITNEANDTITHEHEREDIONMEHIWAALLATINGIONRENEVERESTHEVEVEINMEHENERENDWAOURSTTHI

# Challenge Output

    THER
    THI
    ES
    OUL
    EVER
    EOMEH

# Bonus

Can you find the longest common substring of any pair of words in this Limerick poem?

    There was a young rustic named Mallory,
    who drew but a very small salary.
      When he went to the show,
      his purse made him go
    to a seat in the uppermost gallery.

# Scala Solution

    def LCS(a:String, b:String): String = {
        def substrings(s:String): List[String] = s.inits.flatMap(_.tails.toList.init).toList
        substrings(a).toSet.intersect(substrings(b).toSet).map(x=>(x.length, x)).toList.sortBy(_._1).map(_._2).last
    }
