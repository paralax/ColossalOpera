# Title

Number of attacked squares in Chess

# Difficulty

Hard

#Description 

[Chess](https://en.wikipedia.org/wiki/Chess) is a popular board game. The objective is to use chess pieces to eliminate those of your opponent and *checkmate* their king (one of the pieces) so that it can't move in any direction without being threatened. The game is played on an 8x8 board with letters A-H denoting columns and numbers 1-8 denoting rows:

      +-+-+-+-+-+-+-+-+
    8 |R| | | | | | | |
      +-+-+-+-+-+-+-+-+ 
    7 | | | | | | | | | 
      +-+-+-+-+-+-+-+-+ 
    6 | | | | | | | | | 
      +-+-+-+-+-+-+-+-+ 
    5 | | | | | | | | | 
      +-+-+-+-+-+-+-+-+ 
    4 | | | | | | | | | 
      +-+-+-+-+-+-+-+-+
    3 | | | | | | | | | 
      +-+-+-+-+-+-+-+-+ 
    2 | | |X|X|X| | | | 
      +-+-+-+-+-+-+-+-+ 
    1 | | |X|K|X| | | | 
      +-+-+-+-+-+-+-+-+ 
       A B C D E F G H 

On the board above the square with 'K' is D1, and the square with 'R' is A8. 

There are six types of chess pieces: 

* King (`K`) 
* Queen (`Q`) 
* Rook (`R`) 
* Bishop (`B`) 
* Knight (`N`) 
* Pawn (`P`) 

Each of them can move only in a specific way. For instance, Pawn can move only forward by one square and Queen can move in any direction (left, right, forwards or backwards) by any number of squares. If you're not familiar with rules of chess, check out [wikipedia page on chess pieces](https://en.wikipedia.org/wiki/Chess_piece#Moves_of_the_pieces). 

Let's assume that a square is **attacked** by a chess piece if it can legally move on this square in one move. For instance the King on the board above attacks five squares (`C1`, `C2`, `D2`, `E2` and `E1`) marked with `X`. For this challenge, write a program which calculates how many squares are attacked by a chess piece in a given position. 

# Input description 

The input will consist of one-letter representation of a chess piece and its position on the board. 

# Output description 

Output can be as extensive as you wish. The minimum is a single number denoting number of squares attacked by the piece. You may also include their coordinates, or even print an ASCII representation of the board, marking the attacked squares with `X` - sky is the limit! 

# Sample input 

    R D3
    B B6
# Sample output 
    14 
    9 
# Challenge input 

    K E6
    K G4
    P G5
    R F2
    B A2
    N E2
    K C2
    R A8
    B F7
    Q D1
    B B8
    Q C7
    P E8
    K F4
    N G2

# Notes 

* Assume that there is always exactly one chess piece on the board. 
* Pieces are moved from your perspective, i.e. at the initial state of the board, your pieces would be placed in rows 1-2 
* For consistency, don't account for special cases, like pawn being able to move two squares forward from its initial position. The correct output for `P B2` is `1`. If, however, you decide to account for special cases, you should state so in the comment. 

# Bonus 

Make your program accept an arbitrarily large board size.
