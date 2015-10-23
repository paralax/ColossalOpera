# Title

Capitalize The First Letter of Every Word

# Difficulty

Easy

# Description

Given a sentence, can you capitalize the first letter of every word? 

Yes this is a built-in in Python (`string.capwords`) and maybe some other languages, but the challenge is to implement your own `capwords`-like method. 

# Input Description

You'll be given an Enlish language sentence like this:

    Now is the time for all great programmers to capitalize the correct words.

# Output Description

You should emit a sentence with the first letter of every word capitalized. 

    Now Is The Time For All Great Programmers To Capitalize The Correct Words.
    
# Challenge Input

    Education is an admirable thing, but it is well to remember from time to time that nothing that is worth knowing can be taught.
    An intelligent man is sometimes forced to be drunk to spend time with his fools.
    The heart of a mother is a deep abyss at the bottom of which you will always find forgiveness.
    All things are subject to interpretation whichever interpretation prevails at a given time is a function of power and not truth.

# Challenge Output

    Education Is An Admirable Thing, But It Is Well To Remember From Time To Time That Nothing That Is Worth Knowing Can Be Taught.
    An Intelligent Man Is Sometimes Forced To Be Drunk To Spend Time With His Fools.
    The Heart Of A Mother Is A Deep Abyss At The Bottom Of Which You Will Always Find Forgiveness.
    All Things Are Subject To Interpretation Whichever Interpretation Prevails At A Given Time Is A Function Of Power And Not Truth.

# Scala Solution

    def capwords(s:String) = s.split(" ").map(x => x.slice(0,1).toUpperCase + x.slice(1,x.length)).mkString(" ")
