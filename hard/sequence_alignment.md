#Title 
DNA and Protein Sequence Alignment

#Difficulty 
Hard

#Description

If you are studying a particular pair of genes or proteins, an important question is to what extent the two sequences are similar. To quantify similarity, it is necessary to align the two sequences, and then you can calculate a similarity score based on the alignment.

There are two types of alignment in general. A global alignment is an alignment of the full length of two sequences, for example, of two protein sequences or of two DNA sequences. A local alignment is an alignment of part of one sequence to part of another sequence.

Alignment treats the two inputs as a linear sequence to be lined up as much as possible, with optional gaps and conversions allowed. The goal is to minimize these differences. 

The first step in computing a alignment (global or local) is to decide on a scoring system. For this exercise, we'll simplify this and give a score of +2 to a match and a penalty of -1 to a mismatch, and a penalty of -2 to a gap. 

For more information and how to do this using an R package, see the chapter "Pairwise Sequence Alignment" at  http://a-little-book-of-r-for-bioinformatics.readthedocs.org/en/latest/src/chapter4.html. The key algorithm is Needleman-Wunsch (http://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm).

For this challenge your task is to write a program that accepts two sequences and globally aligns them. If you want to make this harder and integrate the BLOSUM matrices, you may. 

#Input Description

You'll be given two sequences on two lines, one line per sequence. They'll be the same type of input, DNA or protein. 

#Output Description

Your program should emit the aligned sequences with gaps introduced represented by dashed ("-"). 

#Input

DNA example

    ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTAC
    ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTAC
    
Protein example

    MTNRTLSREEIRKLDRDLRILVATNGTLTRVLNVVANEEIVVDIINQQLLDVAPKIPELENLKIGRILQRDILLKGQKSGILFVAAESLIVIDLLPTAITTYLTKTHHPIGEIMAASRIETYKEDAQVWIGDLPCWLADYGYWDLPKRAVGRRYRIIAGGQPVIITTEYFLRSVFQDTPREELDRCQYSNDIDTRSGDRFVLHGRVFKN
    MLAVLPEKREMTECHLSDEEIRKLNRDLRILIATNGTLTRILNVLANDEIVVEIVKQQIQDAAPEMDGCDHSSIGRVLRRDIVLKGRRSGIPFVAAESFIAIDLLPPEIVASLLETHRPIGEVMAASCIETFKEEAKVWAGESPAWLELDRRRNLPPKVVGRQYRVIAEGRPVIIITEYFLRSVFEDNSREEPIRHQRSVGTSARSGRSICT

#Output

DNA example

    ACGTACGTAC GTACGTACGT ACGTACGTAC GTACGTACGT ACGTACGTAC
    ACGTACGTAC GTACGTACGT ----ACGTAC GTACGTACGT ACGTACGTAC
    
Protein example

    MT-----NR--T---LSREEIRKLDRDLRILVATNGTLTRVLNVVANEEIVVDIINQQLLDVAPKIPELENLKIGRILQRDILLKGQKSGILFVAAESLIVIDLLPTAITTYLTKTHHPIGEIMAASRIETYKEDAQVWIGDLPCWLADYGYWDLPKRAVGRRYRIIAGGQPVIITTEYFLRSVFQDTPREELDRCQYSNDIDTRSGDRFVLHGRVFKN
    MLAVLPEKREMTECHLSDEEIRKLNRDLRILIATNGTLTRILNVLANDEIVVEIVKQQIQDAAPEMDGCDHSSIGRVLRRDIVLKGRRSGIPFVAAESFIAIDLLPPEIVASLLETHRPIGEVMAASCIETFKEEAKVWAGESPAWLELDRRRNLPPKVVGRQYRVIAEGRPVIIITEYFLRSVFEDNSREEPIRHQRS--VGT-SA-R---SGRSICT

#Notes

Have a cool challenge idea? Post it to /r/DailyProgrammer_Ideas!
