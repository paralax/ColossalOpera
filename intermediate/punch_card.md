# Title

Punch Card Creator

# Difficulty

Intermediate

# Description

Punch (or punched) cards are an archaic form of recording instruction. Many people here may think of them from the early digital computing era, but they actually go back to fairground organs and textile mills in the 19th century! The format most of us are familiar with was originally patented by Hollerith, using stiff card stock. Over the years this format changed slightly and varied on this them, including a diagonal cut corner. For this challenge we'll focus on the tail end of punch cards with IBM, GE and UNIVAC type cards. 

To use them, a program would be transcribed to the punch cards. Each column represented a single character, 80 columns to the card, 12 rows to the column. The zone rows can be used to have *two* punches per column. You can visualize it like this:

	                  ____________
	                 /
	          /  12 / O
	  Zone rows  11|   O
	          \/  0|    O
	          /   1|     O
	         /    2|      O
	        /     3|       O
	  Numerc      4|        O
	  rows        5|         O
	        \     6|          O
	         \    7|           O
	          \   8|            O
	           \  9|             O
	               |______________

Each card vendor would have an alphabet, an array of characters that are numerically represented by the punches. Here's a simple example with a simple alphabet:

	     ______________________________________________
	    /&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ
	 Y / x           xxxxxxxxx
	 X|   x                   xxxxxxxxx
	 0|    x                           xxxxxxxxx
	 1|     x        x        x        x
	 2|      x        x        x        x
	 3|       x        x        x        x
	 4|        x        x        x        x
	 5|         x        x        x        x
	 6|          x        x        x        x
	 7|           x        x        x        x
	 8|            x        x        x        x
	 9|             x        x        x        x
	  |________________________________________________

You can see the first 12 characters are represented by a single punch, then the next 9 have two punches (with one in the upper zone), then the next 9 use the next zone as that second punch, then the final 9 use the third zone and another punch to indicate the character. 

For some more information, including frm where some of this info was taken, please see http://homepage.cs.uiowa.edu/~jones/cards/codes.html or Wikipedia http://en.wikipedia.org/wiki/Punched_card . 

So, given an alphabet array you should be able to encode a message in a punch card, right? Let's go back to the punch card!

# Input Description

You'll be given a single integer *N* telling you how many alphabets to read. Then you'll be given *N* rows of a description and an alphabet array describing the punch card, then asked to represent a short message on a specific type of punch card.

# Output Description

Your program should emit an ASCII art punchcard  in the format above, with the diagonal notch and everything, and the message across the top. 

# Challenge Input

	4
	CDC  +-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:=±<%[<.)>¬;v$*|¦>],(a=^
	029  &-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@'="¢.<(+|!$*);¬ ,%_>?
	1108 +-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ&=':>@·.)[<#·$*];^±,(%\¤
	GE   &-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ[#@:>?+.](<\^$*);'_,%="!
	2
	Hello, world!
	This is Reddit's r/dailyprogrammer challenge. 
	WRITE (6,7) FORMAT(13H HELLO, WORLD) STOP END

# Challenge Output