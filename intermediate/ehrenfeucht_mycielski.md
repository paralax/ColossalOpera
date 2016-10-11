# Title

The Ehrenfeucht-Mycielski sequence (0,1-version)

# Difficulty

Intermediate

# Tags

binary sequence, infinite sequence

# Description

The [Ehrenfeucht–Mycielski sequence](https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Mycielski_sequence) is a recursively defined sequence of binary digits with pseudorandom properties, defined by Andrzej Ehrenfeucht and Jan Mycielski. The sequence starts with the single bit 0; each successive digit is formed by finding the longest suffix of the sequence that also occurs earlier within the sequence, and complementing the bit following the most recent earlier occurrence of that suffix. (The empty string is a suffix and prefix of every string.)

Additional information is available from [the On-Line Encyclopedia of Integer Sequences](https://oeis.org/A038219), under entry A038219. 

The first three terms of the sequence are "010". The fourth term is calculated as follows: The suffix "0" of "010" occurs earlier, most-recently followed by a 1, so add 0, yielding "0100". 

Your challenge today is to write a generator for this sequence. 

If you want to check your work, [pre-calculated sequences are available up to a million terms](http://barnyard.syr.edu/mseq/mseq.shtml). 
