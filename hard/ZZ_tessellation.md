# Title

[2018-07-13] Challenge #365 [Hard] Tessellations and Tilings

# Difficulty

Hard

# Tags

art, tessellations

# Description

A *Tessellation* (or Tiling) is the act of covering a surface with a pattern of flat shapes so that there are no overlaps or gaps. Tessellations express fascinating geometric and symmetric properties as art, and famously appear in Islamic art with four, five, and six-fold regular tessellations.

Today we'll your challenge is to write a program that can do basic regular tessellations in ASCII art. 

# Input Description

You'll be given an integer on the first line, which can be positive or negative. It tells you the rotation (relative to clockwise, so 180, 90, 0, or -90) to spin the tile as you tessellate it. The next line contains a single integer that tells your program how many columns and rows to read (assume it's a square). Then the next _N_ rows contain the pattern of the tile in ASCII art. 

Example:

    90
    4
    ####
    #--#
    #++#
    ####

# Output Description

Your program should emit a tessellation of the tile, with the rotation rules applied, repeated _at least two times in both the horizontal and vertical directions_, you can do more if you wish. For the above:

    ########
    #--##+|#
    #++##+|#
    ########
    ########
    #+|##++#
    #+|##--#
    ########

# Challenge Input


    90
    6
    /\-/|-
    /\/-\/
    ||\\-\
    |\|-|/
    |-\|/|
    |\-/-\

----

    180
    6
    &`{!#;
    #*#@+#
    ~/}}?|
    '|(==]
    \^)~=*
    |?|*<%
