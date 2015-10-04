# Title

XOR Decoding

# Difficulty

Easy

# Description

One of the simplest ways to obfuscate text is to XOR a single byte value over the input data. This is not uncommon in malware, for example. If you know you have text strings in there, even better a *particular* text string, you can use that to test for the correct XOR value.

For example, take the following string in hex encoding (using ASCII values for characters):

    0x6a 0x67 0x6e 0x6e 0x6d 0x22 0x75 0x6d 0x70 0x6e 0x66

Or in ASCII:

    jgnnm"umpnf

This is XOR encoded with 0x02, so we can decode it the same way:

    j XOR 0x2 = h
    g XOR 0x2 = e
    ...

yielding "hello world". 

## Decoding Notes

You may want to think about how to decide if it's decoded. Perhaps letter frequencies, dictionary lookups, etc. 

# Input Description

You'll be given an input string that has been XOR encoded (with a single byte). 

# Output Description

Your program should emit the XOR byte value and the decoded string. 

# Challenge Input

    Sont'wuh`ufj'dfiihs'eb'uri'ni'CHT'Jhcb)
    jvvr8--uuu,pgffkv,amo-p-fckn{rpmepcoogp

# Challenge Output

    0x07 This program cannot be run in DOS Mode.
    0x02 http://www.reddit.com/r/dailyprogrammer
    
