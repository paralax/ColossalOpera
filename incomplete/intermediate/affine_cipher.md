# Title

Affine Cipher or Caeser + 1

# Difficulty

Intermediate

# Description

The Caesar Cipher has already been covered on this sub several times ([1](https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/?ref=search_posts) [2](https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/?ref=search_posts)). The concept is simple: shift the alphabet over by a few spaces. However, this has its problems. There are only 26 possible keys which makes cracking it with brute force relatively easy (albeit time-consuming), even without a computer. It's also susceptible to frequency analysis: with a long enough message, the most common letter will always be 'e' (at least in English), and once you've found the 'e', counting back five steps gives you the 'a' and the key.

The next step up is the Affine Cipher, which is able to use more keys and throws up problems for frequency analysis.

Encrypting with the affine cipher is pretty easy. You find the position of your letter, multiply by your first key (the multiplicative key), then add an additive key.

For example:

    "Hello world", 

with an additive key of 21 and a multiplicative key    of 3 gives:

    QHCCL JLUCE

Note: additive keys higher than 26 are pointless, and the multiplicative key and the alphabet length (26 in most cases) must be coprime (they have no common factors other than 1)

# Challenges

1. Include a decoder. Decoding isn't as simple as subtracting the additive key (akey) and dividing by the multiplicative key (mkey). Instead of dividing, you need to multiply by the mkey's inverse. That's the number you multiply the mkey by to get 1 in modulo 26.

2. Output the ciphertext (encrypted message) spaced in blocks of five to throw off word-length analysis. For example, this message becomes:

    OUTPU TTHEC IPHER TEXT( ENCRY PTEDM...

3. Include a message breaker. This should be able to take any affine-encoded text and return it as normal English without the key.

Hint: The best way I've found of doing this is finding the most common letter, and assuming it's E. You can then use that to generate a list of possible keys that would turn E into that letter.
