DNA is the building block of every organism. It contains information about  hair colour, skin tone, allergies, what you like, what you don't like and more.
[It's usually visualized as a long double helix of base pairs.](http://cdn.theatlantic.com/static/mt/assets/science/shutterstock_34693498%20copy.jpg) This is all very simply put and I'm missing a lot of extra information but for now this is all you need to know.
The base pairs are as follows: A-T and G-C.

Meaning: on one side of the strand there may be a series of bases 

    A T A A G C 

And on the other strand there will have to be

    T A T T C G

It is your job to generate one side of the DNA strand and output the two DNA strands.


#Generated

    A A T G C C T A T G G C

#Output
    A A T G C C T A T G G C
    T T A C G G A T A C C G

**Extra Intermediate**

Three base pairs make a codon. These all have different names based on what combination of the base pairs you have. A handy table can be found [here](http://en.wikipedia.org/wiki/DNA_codon_table).
The string of codons starts with an ATG (Met) codon ends when a STOP codon is hit.

**Exercise**

Implement functionality for naming the codons, and that every generated DNA strand starts with a Met codon and ends with a STOP codon.

#Generated

    A T G T T T C G A G G C T A A

#Output

    A T G T T T C G A G G C T A A
    Met Phe Arg Gly STOP

#Credit

Thanks to /u/wickys for the submission.
