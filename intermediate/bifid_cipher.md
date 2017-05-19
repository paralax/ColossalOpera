# Title

Bifid Cipher

# Difficulty

Intermediate

# Tags

cipher

# Description

The [Bifid cipher](https://en.wikipedia.org/wiki/Bifid_cipher), invented around 1901 by Felix Delastelle,  is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion. 

To encipher a message, you first draw up a Polybius square of letters. Typically you have to combine two letters to get a 5x5 square, so we'll combine I and J:

|     | 1 | 2 | 3 | 4 | 5 |
| ----|---|---|---|---|---|
| **1** | B | G | W | K | Z |
| **2** | Q | P | N | D | S | 
| **3** | I | O | A | X | E |
| **4** | F | C | L | U | M |
| **5** | T | H | Y | V | R |

The message is converted to its coordinates (column and row), but they are written vertically beneath:

    F L E E A T O N C E
    4 4 3 3 3 5 3 2 4 3
    1 3 5 5 3 1 2 3 2 5

These numbers are then read out as *rows*:

    4 4 3 3 3 5 3 2 4 3 1 3 5 5 3 1 2 3 2 5

These numbers are then grouped into pairs and then turned back into letters using that Polybius square:

    44 33 35 32 43 13 55 31 23 25
    U  A  E  O  L  W  R  I  N  S

To decrypt, the procedure is simply reversed.

Today's challenge is to implement the Bifid cipher:

- Implement enciphering and deciphering.
- Your implementation should accept both a Polybius square and a message to encipher or decipher. You don't want to keep using the same square for all messages, that would defeat the security.
