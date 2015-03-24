Continuing with our bioinformatics theme today. If you like these sorts of problems, I encourage you to check out Project Rosalind (their site seems back up): http://rosalind.info/problems/locations/

# Title 

[2015-03-25] Challenge #207 [Intermediate] Bioinformatics 2: DNA Restriction Enzymes

# Difficulty

Intermediate

# Description

Restriction enzymes are DNA-cutting enzymes found in bacteria (and harvested from them for use). Because they cut within the molecule, they are often called restriction endonucleases. In order to be able to sequence DNA, it is first necessary to cut it into smaller fragments. For molecular biology work, what is needed is a way to cleave the DNA molecule at a few precisely-located sites so that a small set of homogeneous fragments are produced. The tools for this are the restriction endonucleases. The rarer the site it recognizes, the smaller the number of pieces produced by a given restriction endonuclease.

Today your challenge is to write a program that can recognize 

# Input

You'll be given a list of DNA restriction enzymes and their recognition site and where the cut occurs. The input will be structured as enzyme name, if the enzyme makes a "sticky" or "blunt" end cut, the DNA recognition sequence and the position of the cut marked with a carrot ("^"). For the sticky ends, you should assume the mirror image of the complementary strand gets the same cut, leaving one of the strands to overhang (hence it's "sticky"). 

Example:

	BamHI sticky G^GATCC
	HaeIII blunt GG^CC
	HindIII sticky A^AGCTT

Then you'll be given a DNA sequence and be asked to cut it with the listed enzymes. For sake of convenience, the DNA sequence is broken into blocks of 10 bases at a time and in lengths of 6 blocks per row. You should merge these together and drop the first column of digits.

This sequence was taken from Enterobacteria phage phiX174 sensu lato, complete genome http://www.genome.jp/dbget-bin/www_bget?refseq+NC_001422 and modified for this challenge. 

	  1 gagttttatc gcttccatga cgcagaagtt aacactttcg gatatttctg atgagtcgaa
	 61 aaattatctt gataaagcag gaattactac tgcttgttta cgaattaaat cgaagtggac
	121 tgctggcgga aaatgagaaa attcgaccta tccttgcgca gctcgagaag ctcttacttt
	181 gcgacctttc gccatcaact aacgattctg tcaaaaactg acgcgttgga tgaggagaag
	241 tggcttaata tgcttggcac gttcgtcaag gactggttta gatatgagtc acattttgtt
	301 catggtagag attctcttgt tgacatttta aaagagcgtg gattactatc tgagtccgat
	361 gctgttcaac cactaatagg taagaaatca tgagtcaagt tactgaacaa tccgtacgtt
	421 tccagaccgc tttggcctct attaagctta ttcaggcttc tgccgttttg gatttaaccg
	481 aagatgattt cgattttctg acgagtaaca aagtttggat ccctactgac cgctctcgtg
	541 ctcgtcgctg cgttgaggct tgcgtttatg gtacgctgga ctttgtggga taccctcgct
	601 ttcctgctcc tgttgagttt attgctgccg tcaaagctta ttatgttcat cccgtcaaca
	661 ttcaaacggc ctgtctcatc atggaaggcg ctgaatttac ggaaaacatt attaatggcg
	721 tcgagcgtcc ggttaaagcc gctgaattgt tcgcgtttac cttgcgtgta cgcgcaggaa
	781 acactgacgt tcttactgac gcagaagaaa acgtgcgtca aaaattacgt gcggaaggag
	841 tgatgtaatg tctaaaggta aaaaacgttc tggcgctcgc cctggtcgtc cgcagccgtt

# Output

Your program should emit the positions of the cuts by enzyme. For the above the solution would be:

	BamHI 517
	HaeIII 435
	HindIII 445
	HindIII 635
	
# Notes

If you have your own idea for a challenge, submit it to /r/DailyProgrammer_Ideas, and there's a good chance we'll post it.