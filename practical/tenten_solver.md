# Title

TenTen (1010) Game Solver

# Difficulty

Hard

# Tags

puzzle, strategy, tenten, 1010

# Description

TenTen (1010) is a new, minimalistic [puzzle game](http://1010ga.me/) for mobile devices (Android, iOS). Your challenge this week is to write a solver: implement some strategy to win. 

The game's rules:

- The board is a 10x10. It opens with all grid squares unclaimed. 
- You're have a stream of pieces, you receive them in batches of 3. You can play the three in any order by placing them on the board. You must clear all three to receive the next batch.
- To place a piece you have to find open grid positions where it can fit - no overlaps allowed. This is somewhat similar to Blockus or Polyominoes. 
- Pieces may not be rotated. This is distinctly unlike Tetris. 
- The game is similar to Tetris in that when you get a line of ten across you clear that line (a row or a column). 
- The game ends when you can't place a piece.

Scoring:

- For each piece placed, you get *N* points where *N* is the total area of the piece.
- For each row cleared you get 10 points per row. Multiple row clears at once further multiply that by the number of rows. For example: you clear 2 rows, so that's 2 * 10 * 2 or 80 points - two rows at ten points per row times a bonus of 2.

For this challenge we'll use a common batch of pieces - you may not look ahead and only at the batch of three you're assigned to work on at this step. Again - no looking ahead, you only have the game board and the current batch of three pieces as your knowledge inputs for the functions to place to piece. You can't "unwind" a piece once you've played it, and you can't go back a batch either.

Let's compete and see how many points your strategy can yield. Show your code, too. Try and maximize your points, play with various strategies. 

# Meet The Pieces

    #
    
    ##
    
    #
    #
    
    #
    ##
    
     #
    ##
    
    ##
    #
    
    ##
     #
    
    ##
    ##
    
    ###
    ###
    ###
    
    ####
    ####
    ####
    ####
    
    ###
    
    ####
    
    #####
    
    #
    #
    #
    
    #
    #
    #
    #
    
    #
    #
    #
    #
    #
    
    ####
    #
    #
    #
    
    ####
       #
       #
       #
    
    #
    #
    #
    ####
    
       #
       #
       #
    ####
    
    #
    #
    ###
    
      #
      #
    ###
    
    ###
    #
    #
    
    ###
      #
      #

# The Game Stream

