# Title

[2018-01-19] Challenge #347 [Hard] Hue Drops Puzzle

# Difficulty

Hard

# Tags

game, graph theory

# Description

I found the game [Hue Drops](https://apkpure.com/hue-drops/aero.woi.huedrops) on a recent flight, turns out it's also a mobile game. [One reviewer](https://www.kotaku.com.au/2017/06/every-game-in-my-delta-airplane-seat-reviewed/) described it:

_You start with one dot, and you can change the colours of the adjacent dots. It's like playing with the paint bucket tool in MS Paint! You slowly change the colour of the entire board one section at a time._

The puzzle opens with a group of tiles of six random colors. The tile in the upper left remains wild for you to change. Tile colors change by flooding from the start tile to directly connected tiles in the four cardinal directions (not diagonals). Directly connected tiles convert to the new color, allowing you to extend the size of the block. The puzzle challenges you to sequentially change the color of the root tile until you grow the block of tiles to the target color in 25 moves or fewer.

Today's challenge is to read a board tiled with six random colors (R O Y G B V), starting from the wild (W) tile in the upper left corner and to produce a sequence of color changes 

# Input Description

You'll be given a row of two integers telling you how many columns and rows to read. Then you'll be presented the board (with those dimensions) as ASCII art, each tile color indicated by a single letter (including the wild tile as a W). Then you'll be given the target color as a single uppercase letter. Example:

    4 4 
    W O O O 
    B G V R
    R G B G
    V O B R
    O

# Output Description

Your program should emit the sequence of colors to change the puzzle to achieve the target color. Remember, you have only 25 moves maximum in which to solve the puzzle. Note that puzzles may have more than one solution. Example:

    O G O B R V G R O

# Challenge Input

    10 12
    W Y O B V G V O Y B
    G O O V R V R G O R
    V B R R R B R B G Y
    B O Y R R G Y V O V
    V O B O R G B R G R
    B O G Y Y G O V R V
    O O G O Y R O V G G
    B O O V G Y V B Y G
    R B G V O R Y G G G
    Y R Y B R O V O B V
    O B O B Y O Y V B O
    V R R G V V G V V G
    V
