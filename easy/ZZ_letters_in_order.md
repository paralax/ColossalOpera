# Title

Letters in Alphabetical Order

# Difficulty

Easy

# Tags

word games, alphabet

# Description

A handful of words have their letters in alphabetical order, that is nowhere in the word do you change direction in the word if you were to scan along the English alphabet. An example is the word "almost", which has its letters in alphabetical order.

Your challenge today is to write a program that can determine if the letters in a word are in alphabetical order.

As a bonus, see if you can find words spelled in *reverse* alphabetical order. 

# Input Description

You'll be given one word per line, all in standard English. Examples:

	almost
	cereal

# Output Description

Your program should emit the word and if it is in order or not. Examples:

	almost IN ORDER
	cereal NOT IN ORDER

# Challenge Input

	billowy
	biopsy
	chinos
	defaced
	chintz
	sponged
	bijoux
	abhors
	fiddle
	begins
	chimps
	wronged

# Challenge Output

	billowy IN ORDER
	biopsy IN ORDER
	chinos IN ORDER
	defaced NOT IN ORDER
	chintz IN ORDER
	sponged REVERSE ORDER 
	bijoux IN ORDER
	abhors IN ORDER
	fiddle NOT IN ORDER
	begins IN ORDER
	chimps IN ORDER
	wronged REVERSE ORDER

# Scala Solution

    def alphabetical(word:String): Boolean = word.map(_.toInt).sorted == word.map(_.toInt)
    def rev_alphabetical(word:String): Boolean = word.map(_.toInt).sorted.reverse == word.map(_.toInt)

    def main(word:String) = {
        if (alphabetical(word) == true) 
            println(word + " IN ORDER")
        else if (rev_alphabetical(word) == true) 
            println(word + " IN REVERSE ORDER")        
        else
            println(word + " NOT IN ORDER")
    }