# Title

(Practical Exercise): Fuzzy Sets

## Background

In mathematics, fuzzy sets are sets whose elements have degrees of membership. Fuzzy sets were introduced by Lotfi A. Zadeh and Dieter Klaua in 1965 as an extension of the classical notion of set.

Fuzzy sets are composed of fuzzy numbers. A fuzzy number is an generalization of a regular, real number in the sense that it does not refer to one single value but rather to a connected set of possible values, where each possible value has its own weight between 0 and 1. This weight is called the membership function. Some examples of fuzzy numbers are

    {4, .25}
    {-5, 1}
    {-1, 1}

In classical set theory, the membership of elements in a set is assessed in binary terms according to a bivalent condition — an element either belongs or does not belong to the set. By contrast, fuzzy set theory permits the gradual assessment of the membership of elements in a set; this is described with the aid of a membership function valued in the real unit interval [0, 1]. Fuzzy sets generalize classical sets, since the indicator functions of classical sets are special cases of the membership functions of fuzzy sets, if the latter only take values 0 or 1. In fuzzy set theory, classical bivalent sets are usually called crisp sets. The fuzzy set theory can be used in a wide range of domains in which information is incomplete or imprecise, such as bioinformatics.

For additional information, see these references: 
- http://www.sjsu.edu/faculty/watkins/fuzzysets.htm
- http://reference.wolfram.com/applications/fuzzylogic/index2.html

# Specification

You are to implement a class (or similar interface for your language) representing a fuzzy set. It should support the following methods or operations on that fuzzy set:

- Equality of two fuzzy sets
- Union of two fuzzy sets
- Intersection of two fuzzy sets

