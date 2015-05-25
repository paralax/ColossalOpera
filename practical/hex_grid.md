# Title

Hex Grid Implementation

# Description

A handful of games like "Hex" and "Settlers of Catan" use hex cells in their games. Unlike a square grid, a hex grid has constant distance between the center and its neighbors. This makes it especially useful for war games and other maneuver games. The hex map has been a favourite for game designers since 1961, when Charles S. Roberts of the Avalon Hill game company published the second edition of Gettysburg with a hex map.

The nature of a hexagonal layout means that your neighbors aren't represented by a simple "up/down" and "left/right" pair. No hex cell has an adjacent hex cell lying directly "east" or "west", making movement in a straight line east or west somewhat more complicated than on a square grid map. Instead, paths in these directions, and any other path that does not bisect one of the six cell edges, will "zig-zag"; since no two directions are orthogonal, it is impossible to move forward in one direction without moving backwards slightly in the other.

Hex grids uses a trapezoidal/axial coordinate system. The axis' look a little different depending on flat or pointed orientation.

Flat orientation:

              _ _
            /     \
       _ _ /(0,-1) \ _ _
     /     \  -R   /     \
    /(-1,0) \ _ _ /(1,-1) \
    \  -Q   /     \       /
     \ _ _ / (0,0) \ _ _ /
     /     \       /     \
    /(-1,1) \ _ _ / (1,0) \
    \       /     \  +Q   /
     \ _ _ / (0,1) \ _ _ /
           \  +R   /
            \ _ _ /

Pointy orientation:

           / \     / \
         /     \ /     \
        | -1,-1 |  1,-1 |
        |   -R  |       |
       / \     / \     / \
     /     \ /     \ /     \
    | -1,0  |  0,0  |  1,0  |
    |  -Q   |       |   +Q  |
     \     / \     / \     /
       \ /     \ /     \ /
        | -1,1  |  0,1  |
        |       |   +R  |
         \     / \     /
           \ /     \ /

For this challenge you should implement code to genearte a hex grid with the following requirements:

* Set the size of the hex grid in heighth and width
* Set the orientation (pointy or flat) of the grid
* Support moving from one tile to another (left, right, up, down, diagonal) 
* Display the hex grid with tiles labeled

# Notes 

http://www.redblobgames.com/grids/hexagons/
