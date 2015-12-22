# Title

Typo Maker

# Difficulty

Easy

# Tags

word play

# Description

Typos are great fun, and often follow a common pattern - keys next to eachother, doubled or omitted characters, and transpositions. Can you write a program to generate common typos? If so, you could be on your way to typo-squatting in DNS!

Common typos fall into a few different categories:

* Skip letter
* Double letters
* Reverse (transpose) letters
* Skip spaces
* Missed key
* Inserted key

For this challege, when you think about neighbor keys, assume a QWERTY keyboard layout (http://en.wikipedia.org/wiki/QWERTY). 

# Input Description

You'll be given a word, one per line, and asked to generate typos for it. Example:

    typo

# Output Description

Your program should emit the word mangled into its various formats using the above categories. Our example:

    tpo
    ypo
    typ
    ttypo
    tyypo
    typpo
    typoo
    tyop
    ytpo
    toyp
    rypo
    yypo
    ttpo
    tupo
    ty[o
    tyoo
    typi
    typp
    trypo
    rtypo
    ... (omitted for brevity)

# Input Description

    Facebook
    Google
    Global thermonuclear war
    Dead as a doornail
    Britney Spears
    Cappuccino
    Everybody to the limit
