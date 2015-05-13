# Title

Hex Grid Implementation

# Description

Hex grids uses a trapezoidal/axial coordinate system. The axis' look a little different depending on flat or
pointed orientation.

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
