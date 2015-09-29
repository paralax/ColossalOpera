# Title

Anagram Detector

# Difficulty

Easy

# Description

An anagram is a word (or set of words) that use the same letters just rearranged. All words must be valid spelling. Someone once said, "All the life's wisdom can be found in anagrams. Anagrams never lie." How they don't lie is beyond me, but there you go. Punctuation and capitalization don't matter. 

# Input Description

You'll be given two words or sets of words separated by a question mark. Your task is to replace the question mark with information about the validity of the anagram. Example:

    "Clint Eastwood" ? "Old West Action"
    "parliament" ? "partial man"

# Output Description

You should replace the question mark with some marker about the validity of the anagram proposed. Example:

    "Clint Eastwood" is an anagram of "Old West Action"
    "parliament" is NOT an anagram of "partial man"

# Challenge Input

    "wisdom" ? "mid sow"
    "Seth Rogan" ? "Gathers No"
    "Reddit" ? "Eat Dirt"
    "Schoolmaster" ? "The classroom"
    "Astronomers" ? "Moon starer"
    "Vacation Times" ? "I'm Not as Active"
    "Dormitory" ? "Dirty Rooms"

# Challenge Output

    "wisdom" is an anagram of "mid sow"
    "Seth Rogan" is an anagram of "Gathers No"
    "Reddit" is NOT an anagram of "Eat Dirt"
    "Schoolmaster" is an anagram of "The classroom"
    "Astronomers" is NOT an anagram of "Moon starer"
    "Vacation Times" is an anagram of "I'm Not as Active"
    "Dormitory" is NOT an anagram of "Dirty Rooms"

# Scala Solution

    def anagram(s1:String, s2:String): Boolean = s1.toLowerCase().filter(_.isLetter).sorted == s2.toLowerCase().filter(_.isLetter).sorted
