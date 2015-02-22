**Title** Coiled sentence

**Difficulty** Hard

**Description**

You'll be given a matrix of letters that contain a coiled sentence. Your program should walk the grid to adjacent squares using only left, right, up, down (no diagonal) and every letter exactly once. You should wind up with a six word sentence made up of regular English words.

Your input will be a list of integers *N*, which tells you how many lines to read, then the row and column (indexed from 1) to start with, and then the letter matrix beginning on the next line.  

**Input**

        6 1 1
        T H T L E D 
        P E N U R G
        I G S D I S
        Y G A W S I 
        W H L Y N T
        I T A R G I

(Start at the T in the upper left corner.)

**Expected Output** 

        THE PIGGY WITH LARYNGITIS WAS DISGRUNTLED

**Challenge Input**

    5 1 1
    I E E H E
    T K P T L
    O Y S F I 
    U E C F N
    R N K O E

(Start with the I in the upper left corner)

**Challenge Output**

    IT KEEPS YOUR NECK OFF THE LINE
