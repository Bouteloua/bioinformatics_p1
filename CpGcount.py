#Program 2

#Another signal of a gene is called "CpG islands". The "p" refers to the phosphodiester bond connecting the cytosine to the guanine nucleotide, reading in the normal 5' to 3' direction. http://en.wikipedia.org/wiki/CpG_site#CpG_islands
#So you want to count "CG" dimers in a sequence. Write a small program called CpGcount.py to do that.


import random

def randomSeq(N):
	bases = "ACTG"
	seq = ""
	for i in xrange(N):
		seq += bases[random.randint(0,3)]

	return seq
	
print "Count \"CG\" dimers in a sequence"
print randomSeq(50).count('CG')