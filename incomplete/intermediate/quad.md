# Title 

Playing a Game of Quad 

# Difficulty

Intermediate

# Tags

game, Quad

# Description

I first read about [Quad](http://everything2.com/user/hobyrne/writeups/Quad) in the pages of Scientific American Volume 274 Number 3, March 1996, with original games rules and concept invented by G. Keith Still. The game is played on a square grid board, 11 by 11. Players both start each game with an infinite number of pieces, and only 7 Quazars, pieces used to block a position from being used by either player. Each turn you may place as many of your Quazars as you want (zero or more), but remember that you only get 7 for the whole game. You complete your move by placing a game piece. 

The objective of Quad is to place one of your pieces at each of the four corners of a square. When you have done this you have made a Quad. A Quad can be in any orientation and of any size. Think of it as a variant of Connect Four. The first player to build a Quad wins.

Your challenge is to read a game and determine the winning move for the next player. 

# Input Description

The board will be defined as an 11x11 grid, with rows as letters (`a`-`k`), and columns as numbers (`1`-`11`). You'll be given a series of moves for each player, with players separated by a pipe character (`|`). If you see multiple pieces played (separated by a comma, `,`), that indicates the player played Quazars, which they can do before playing a piece. Remember: a player can place as many Quazars per turn as they want until they run out, but they cannot move them once played, so they get a maximum of 7. 

For example, a brief series of moves in game might look like this: 

    a1|a2,b8
    b7,a3|c3,c9
    d1|c7
    d4

Here each player played a Quazar (at a2, then b7 and finally c3)in addition to moving (although player 1 didn't play a Quazar in their first move). The above game indicates that player 2 is to move. 

# Output Description

Your program should emit the next move that will give the next player the winning move. From the above example:

    d8

That will give player 2 a winning position. 

# Python Move Generator


    import random
    import string

    cache = set()

    def move(n): 
        m = random.choice(string.lowercase[:10]) + `random.randint(1,11)`
        if m not in cache:
            cache.add(m)
            if (random.random() < 0.1 and n > 0):
                mn, n = move(n-1)
                return (mn + "," + m, n-1)
            return (m, n)
        else:
            return move(n)

    def game(n):
        a = 7
        b = 7        
        for _ in xrange(n): 
            ma, a = move(a)
            mb, b = move(b)
            print ma + "|" + mb
