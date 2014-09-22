#By: Brian Franzone
#Email: Franzone89@gmail.com
#For: Bioinformatics E-100. assignment 1 problem 2
#Summary: Returns the number of GC found in a random sequence. Ignores codon structures.

#Question:
#Another signal of a gene is called "CpG islands". The "p" refers to the phosphodiester bond connecting the cytosine to the guanine nucleotide, reading in the normal 5' to 3' direction. http://en.wikipedia.org/wiki/CpG_site#CpG_islands
#So you want to count "CG" dimers in a sequence. Write a small program called CpGcount.py to do that.

import random

#This function first generates a random sequence.
def randomSeq(N):
	bases = "ACTG"
	#empty string holder
	seq = ""
	#N is the length of the sequence
	for i in xrange(N):
		seq += bases[random.randint(0,3)]
	return seq

#N is the length of the randomly generated sequence
N = 1000
print "Number of CG found are: %i" % randomSeq(N).count('CG')
