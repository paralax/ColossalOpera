# Title

Create a Markdown Table

# Difficulty

Easy

# Description

Markdown has become a common shortcut syntax to create pretty documents, used by Redit, Wikis, and even Github. While mixing the obviousness of text and an interpreted display style, it reads well in both flat text and generated HTML. For this challenge, you'll be tasked with creating a Markdown interpreter to generate tables. The name itself is a play on markup (e.g. HTML), because it's simpler. 

See reddit formatting guidelines on creating a table here: https://www.reddit.com/wiki/commenting or the DaringFireball specification here: http://daringfireball.net/projects/markdown/

For this challenge,  write a function that takes 2 arrays as input: Column headers, and Data, and outputs a markdown table

# Function input

2 arrays native to your language (for data part should handle types other than string). Column headers may be assued to be strings (though why not convert these too?)

# Function Output:

Markdown string, that you can paste into your comment solution to confirm it worked.

# Command line Input

(J syntax for array splitting, first line feed is column headers, rest is rows separated by line feeds)

    Column A ; Column B ; Column C
    A1 ; B1 ; C1
    A2 ; B2 ; C2

# Output

Column A | Column B | Column C 
-|-|-| 
A1 | B1 | C1 
A2 | B2 | C2

# Bonus

You can also set column alignment in markdown. 2 general approaches. Either:
* Modify your column headers to have leading and/or trailing colons (trailing only is right alignment. both leading and trailing is centered).
* Add a 3rd array parameter that codes alignment instruction.

# Notes

This challenge idea was submitted by /u/Godspiral. Have a good challenge idea? Consider submitting it to /r/dailyprogrammer_ideas