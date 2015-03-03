**Title** Trees in the Park

**Difficulty** Intermediate

**Description**

You manage the city parks of beautiful Tree Town. You have a team who loves to plant trees, but have so much pride that they insist their trees be visible by everyone and that no crowding exists. After many contentious meetings you arrive at a compromise: every tree planed must be in its own park, its own row and its own column, and no two trees can be diagonally from each other, either. In doing this, every arborist gets to maximize their tree's enjoyment. 

It's now left to you to plan where these trees will go. 

**Input Description**

You'll be given a single integer *N* which tells you four things: how many rows to read, how many columns to read, how many parks you're working with, and how many trees to plant. You'll then be given the park layout as an ASCII art map with letters indicating the different park designations (e.g. "a", "b", "c" ...). An example map:

    5
    a a b c d
    a a b b d
    e a b d d
    e e e d d
    e e e e e

**Output Description**

Your program should emit the map with the trees planted in the correct spot. Indicate trees with an uppercase "T". For the above example map the solution is:

    a a b T d
    T a b b d
    e a T d d
    e e e d T
    e T e e e

**Challenge Input**

    5
    a b b b b
    a a b b b
    a c d b b
    a d d d e
    a a a e e

**Challenge Output**

    T b b b b
    a a b T b
    a T d b b
    a d d d T
    a a T e e
