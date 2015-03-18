# Title

Happy Numbers

# Difficulty

Easy

# Description

Who knew numbers could be happy? Happy numbers are another topic from mathematics that is pure **fun**!

You are given a number **N**. To determine whether or not it is a happy number, you replace it by the sum of the squares of its digits, repeatedly, until:

**1)** You obtain the number 1, or

**2)** You obtain a number that has been obtained before (so you are in a never-ending loop!)

If you happen to obtain **N=1**, then the original number is a happy number! 

**INPUT**

A natural number **N**.

**OUTPUT**

You should output the string "Happy" if the number is a happy number, else output "Sad".

**EXAMPLE**

Given the number **N = 836**, determine whether it is a happy number:

836 -> 8^2 +3^2 + 6^2 = 109

109   -> 1^2 + 0^2 + 9^2 = 82

82 -> 8^2 + 2^2 = 68

68   -> 6^2 + 8^2 = 100

100  -> 1^2 = **1**

So **836**  is a happy number! 

Let's see what happens when we initially set **N = 740**

740 -> 7^2 + 4^2 = 65

65   -> 6^2 + 5^2 = 61

61   -> (...) = 37

37   -> (...) = 58

58   -> (...) = 89

89   -> (...) = 145

145 -> (...) = 42

42   -> (...) = 20

20   -> (...) = 4

4     -> (...) = 16

16    -> (...) = 37

... But we had already had 37!!! So we are in a loop! Therefore, 740 is not a happy number! 


## FURTHER READING

[**HAPPY NUMBERS**](http://en.wikipedia.org/wiki/Happy_number)

# EXTENSION CHALLENGES

**1)** How many happy numbers are there with **1 &lt;= N &lt;= 1000**?

**2)** Now let's give this problem a small twist. Instead of squaring the digits, take the power as a variable. Which power, from 1 to 10, produces the most happy numbers (with **N** between 1 and 1000)?

# Credit

This challenge idea was submitted by Redditor /u/AnkePluff.

# Notes

Have a cool challenge idea? Post it to /r/DailyProgrammer_Ideas!