# Title

Museum Cameras 1

# Difficulty

Hard

# Description

You run a museum, and you have a small budget - but you have to protect the museum with cameras. Given some descriptions of rooms, can you organize the smallest number of cameras to view the whole room?

Some assumptions and other factors for you to work with:

* Cameras can't see around corners. 
* You can only place cameras in corners.
* Assume every camera has a field of view of 90 degrees, yielding a triangular field of view. 
* Assume every camera's field of view will be equal to the left and right of the line in the corner where the camera is placed; this line bisects the angle of the corner. 
* Assume every camera has an otherwise infinite view.

# Input Description

You'll be given a row with a single number *N* that tells you how many points to read. Then on the next line you'll be given *N* points in a Cartesian coordinate space to draw the bounding box of the museum room. For example:

    3
    (0,0) (3,6) (6,0)

This translates to (pardon my ugly ASCII art) this equliateral triangle:

           .                                       .
                                                  / \
                                =>               /   \
                                                /     \
                                               /       \
                                              /         \
    .             .                          .___________.

# Output Description

Your program should emit the position of the cameras needed to cover the area. From our example:

    (0,0)

That's one possible solution (for this one any of the corners would have worked). 

# Challenge Input

4 
(0,0) (5,0) (5,6) (0,6)

5
(0,0) (7,0) (7,3) (5,6) (0,6)

