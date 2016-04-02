# Title

Scoring a Cribbage Hand

# Difficulty

Intermediate

# Description

Cribbage is a game played with a standard deck of 52 cards. There are several phases or rounds to playing cribbage: deal, discard, play and show. Players can earn points during the play and show rounds. This challenge is specific to the **show** phase of gameplay only. Each player's hand consists of 4 cards and an additional face up card. During the show round, each player scores points based on the content in their hand (plus the face up card). Points are awarded for the following:

* Any number of cards that add up to 15 (regardless of suit) – 2 points
* Runs of 3, 4, or 5 cards – 3, 4 and 5 points respectively 
* Pairs: 2, 3, or 4 of a kind – 2, 6 and 12 points respectively
* Flushes: 4 or 5 cards of the same suit (note, the additional face up card is not counted for a 4 card flush) – 4 and 5 points respectively
* Nobs: A Jack of the same suit as the additional face up card – 1 point

Note: cards can be used more than once, for each combo

# Input Description

Your program should take an array of 5 cards, each card will be designated by a rank: 1 (Ace) - 10 and Q-K as well as a suit: Hearts, Clubs, Spades and Diamonds. The first 4 cards are the cards in your hand and the final card is the additional face up card.

# Output Description

Your program should output the score of the hand

# Sample Input data

* 5D,QS,JC,KH,AC
* 8C,AD,10C,6H,7S
* AC,6D,5C,10C,8C

# Sample Output data

* 10 points (3 fifteens - 6, a run of 3 - 3, and a nob â– 1)
* 7 points (2 fifteens â– 4, a run of 3 â– 3)
* 4 points (2 fifteens â– 4)

# Notes and Further Reading

* [Rules of Cribbage](http://en.wikipedia.org/wiki/Rules_of_cribbage)

# Notes

Many thanks to Redditor /u/codeman869 for this submission to /r/dailyprogrammer_ideas. If you have any ideas, please submit them there!