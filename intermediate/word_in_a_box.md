**Title** Longest Word in a Box

**Difficulty** Intermediate

**Description**

Can you find the shortest path from one corner of a box of letters to another? Here's the rub: the path you take through the box has to spell an English word.

**Input Description** 

You'll be given an integer *N* which tells you how many rows and columns it has (it's a square), and then the box of letters. You can move up, down, left, or right but not diagonally. 

**Output Description**

Starting from the top left corner and ending at the lower right, your program should emit the shortest English language word starting in one corner and ending in the opposite it can find by tracing a path through the box. Optionally show the path it took. 

**Challenge Input**

    11
    b   u       h       l       d       r       t       w       f       v       b
    f   c       j       k       c       k       r       g       k       m       r
    x   k       m       i       n       s       t       f       q       q       w
    d   x       f       n       s       q       e       r       g       h       j
    v   t       w       w       q       t       z       f       u       t       g
    b   r       w       d       l       r       s       a       l       e       e
    n   w       t       q       q       e       x       e       l       h       w
    h   r       q       w       g       w       v       t       e       r       q
    r   r       w       r       t       w       g       y       v       e       n
    w   f       t       h       h       d       h       u       s       j       e
    q   d       y       y       j       n       p       j       w       v       s

**Challenge Output**

        buckminsterfullerenes


