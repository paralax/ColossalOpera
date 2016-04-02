# Title

Dinosaurs

# Difficulty

Hard

#Description 

After a failed genetic engineering experiment a lot of dinosaurs escaped into the lab, devouring most of the staff. Jeff, a scientist that worked on the project, managed to survive by hiding in the southwest corner of the rectangular lab. Now that all dinosaurs are asleep, he tries to leave the lab. 

The exit of the lab is located at its northeast corner. Jeff knows that if any of the dinosaurs wakes up, he does not stand a chance. Thus, he wants to follow a path that maximizes the minimum distance from him to the dinosaurs along the path. The length of the path is of no interest to him. 

In this problem we assume that Jeff and the dinosaurs are points on the plane and that Jeff’s path is a continuous curve connecting the southwest and northeast corners of the lab. As we mentioned, Jeff wants to maximize the minimum distance between this curve and the position of any dinosaur. You can find an example solution for the third test case in the sample input [here](http://imgur.com/duotSll). 

# Formal Inputs & Outputs 

## Input Description 

The input contains several test cases, each consisting of several lines. The first line of each test case contains three integers `N`, `W`, and `H` separated by single spaces. The value `N` is the number of dinosaurs in the lab. The values `W` (width) and `H` (height) are the size of the lab. Jeff starts at `(0, 0)`, while the exit of the lab is located at `(W, H)`. 

Each of the next `N` lines contains two integers `X` and `Y` separated by a single space, representing the coordinates of a dinosaur (`1 ≤ X ≤ W − 1, 1 ≤ Y ≤ H − 1`). Note that no dinosaur is located on the border of the lab. 

## Output Description 

For each test case print a single line with the maximum possible distance to the closest dinosaur rounded to three decimal digits. 

# Sample Inputs & Outputs 

## Input 

    1 2 2 
    1 1 
    3 5 4 
    1 3 
    4 1 
    1 2 
    2 5 4 
    1 3 
    4 1 

## Output 

    1.000 
    1.581 
    1.803 

# Challenge Input 

## Input 

    1 9941 25450
    6409 21339
    10 24024 9155
    2540 8736
    16858 3291
    9647 7441
    1293 1441
    4993 4404
    466 8971
    16447 4216
    20130 6159
    673 2951
    945 2509
    100 27408 715
    5032 102
    16413 326
    14286 454
    10579 623
    16994 320
    4027 384
    26867 483
    22304 416
    2078 633
    19969 205
    262 275
    17725 113
    8781 655
    3343 89
    4982 154
    248 92
    3745 467
    8449 94
    1788 98
    14947 338
    20464 87
    12432 529
    20144 11
    8918 236
    4633 215
    13619 418
    560 461
    23402 29
    15130 55
    23126 28
    2684 131
    2160 690
    17990 464
    988 415
    11740 461
    3112 569
    12758 378
    4311 97
    2297 178
    3576 294
    4453 268
    27326 314
    21007 604
    10478 625
    12402 33
    15347 560
    11906 343
    16774 143
    17634 421
    19842 434
    11606 625
    10228 350
    12667 209
    12658 99
    20918 254
    25007 361
    22634 674
    5196 434
    11630 90
    6128 451
    4783 245
    13210 407
    2928 477
    5686 478
    14826 336
    25711 172
    10835 276
    22725 42
    4408 596
    10719 462
    1743 493
    11042 590
    7568 456
    23426 538
    13890 565
    22168 174
    612 358
    23541 142
    20782 417
    24759 51
    19912 704
    24410 483
    682 168
    22992 311
    9122 8
    16851 109
    10796 484
    15226 395
    4144 456
    763 98
    18293 230
    22287 691
    462 350
    21420 44
    21413 245
    21552 610
    3298 265
    730 16
    25714 231
    16189 298

# Notes/Hints 

- Here is a somewhat larger example (it is still quite small): [Input](http://pastebin.com/gpwsTWg0), [Output](http://pastebin.com/y3siBQvC) that /u/wadehn need ~0.2s for. 
- /u/wadehn [visualized](http://www.scribd.com/doc/236927238) all of the given samples if it helps you debug. (Best download the pdf and do not use the raster images.) 
- /u/wadehn states that their best solution takes `O(N^2*log(W+H))` time and `O(N)` space in the worst case. 

# Credit

This challenge was submitted by /u/wadehn. If you have an idea for a challenge, please share it on /r/dailyprogrammer_ideas.
