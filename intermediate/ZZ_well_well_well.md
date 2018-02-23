# Title

Well, Well, Well

# Difficulty

Intermediate

# Tags

2D array

# Description

A square well is dug with a peculiar shape: each 1x1 section has varying heights above some floor. You wish to fill the well with warer, filling from a hose above the square marked 1. You wish to know when you fill a specific square. 

You can assume water behaves like it does in the real world - it immediately disperses, evenly, to all accessible regions, and it cannot spontaneously leak from one square to another if there is no path. 

Assume a constant flow rate for the water. 

Today's question is - writing a program, can you tell at what time the well's target square is under a cubic unit of water? 

#  Input Description

You'll be given a row with two numbers, N and N, telling you the dimensions of the well. Then you'll be given N rows of N colums of unique numbers. Then you'll get one row with one number, M, telling you the target square to cover with one cubic unit of water. Example:

    3 3
    1 9 6
    2 8 5
    3 7 4
    4

# Output Description

Your program should emit the time unit at which time the target square is covered in one cubic unit of water. 

The above example's answer should be 16. 

Explanation: In this case the column 9 8 7 forms a barrier from the 1 square to the 4 square, our target. As such you have to fill enough to get to a height of 7 to begin filling 4. (7-1) + (7-2) + (7-3) [all to get over the barrier] + 1 [to fill the four block]. 

# Challenge Input

    7 7
      38  33  11  48  19  45  22
      47  30  24  15  46  28   3
      14  13   2  34   8  21  17
      10   9   5  16  27  36  39
      18  32  20   1  35  49  12
      43  29   4  41  26  31  37
      25   6  23  44   7  42  40
    35

----

    7 7
      15  16  46   1  38  43  44
      25  10   7   6  34  42  14
       8  19   9  21  13  23  22
      32  11  29  36   3   5  47
      31  33  45  24  12  18  28
      40  41  20  26  39  48   2
      49  35  27   4  37  30  17
    26
