# Title

Chess Solitaire

# Difficulty

Hard

# Description

Chess solitaire is a variant of chess that sets up puzzles using the pieces and a smaller board. You're given a set of several pieces all of one color, and using the legal moves of those pieces, you're supposed to take them one by one until only one piece is left. The rules state that every move has to be a legal move for that piece, and every move must be a capture of one piece by another. 

Some other differences with regular chess. Again: every move *must* be a capture. For the king, check doesn't matter. There is no "direction" or "forward", anyone can move (within their legal moves) in any direction. Pawns cannot promote, and pawns (as usual) take on the diagonal. 

The board is 4x4, with rows are 1-4 and columns are a-d; the lower left is square a1, so the board looks like this:
    
    d . . . .
    c . . . .
    b . . . .
    a . . . .
      1 2 3 4

The pieces are given by their single character:

- R - rook
- N - knight
- B - bishop
- Q - queen
- K - king
- P - pawn

# Input Description

You'll be given a 4x4 board in ASCII showing the opening board and the pieces positioned on the board. Blank squares are given by a ".". An example:

    R . . R
    . . P .
    . N . . 
    . . . .

# Output Description

You should give the sequence of moves needed to successfully clear the board to one piece using the rules by showing the start square (e.g. "a1") and the captured square (e.g. "b2") joined by an "x". For the above board, the solution would be:

    d4xa4
    b2xa4
    a4xc3
	
Any piece can make the next move *as long as the move results in a legal capture*. 

# Challenge Input

    . N . .
    . . B .
    R . . .
    . . . .

    . . B .
    R . . P
    . R . .
    . P B .

    N . . .
    B P . B
    . . . N
    R R P .
	

# Challenge Output

In order of the above starting boards:

    b4xa2
    a2xc3

    d3xc4
    b2xc4
    c1xa3
    c4xa3
    a3xb1

    d2xb3
    b1xb3
    b3xd3
    d3xa3
    a3xa4
    a4xa1
    a1xc1
