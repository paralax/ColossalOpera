# Title

Math Snake

# Difficulty

Intermediate

# Description

There's a math puzzle making the rounds of the net as of May 2015. According to the VN Express, it was set as a problem for third graders in the town of Bao Loc in the Vietnamese highlands. You need to fill in the gaps with the digits from 1 to 9 so that the equation makes sense, following the order of operations - multiply first, then division, addition and subtraction last.

# Input Description

Rather than making you parse an ASCII snake, you can parse the input as a series of blanks and values. You'll be given operands (`=`, `+`, `-`, `*` and `/`) and numbers together with blanks (as underscores, or `_`) that you need to fill in. 

# Output Description

Your program should emit a solution (multiple solutions may exist) as a valid equation.

# Challenge Input

    _ + 13 * _ / _ + _ + 12 * _ - _ - 11 + _ * _ / _ - 10 = 66

# Challenge Output

    3 + 13 * 2 / 1 + 5 + 12 * 4 - 7 - 11 + 9 * 8 / 6 - 10 = 66

# Notes

This puzzle comes from Alex Bellos at the [Guardian's May 20, 2015 column](http://www.theguardian.com/science/alexs-adventures-in-numberland/2015/may/20/can-you-do-the-maths-puzzle-for-vietnamese-eight-year-olds-that-has-stumped-parents-and-teachers?CMP=share_btn_tw).
