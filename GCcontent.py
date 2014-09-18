#Program 1

#The amount of "GC content" is one of the signals that there is a gene present. http://en.wikipedia.org/wiki/GC-content#GC_ratio_of_genomes
#Write a small program called GCcontent.py to calculate the combined percentage of "C"s and "G"s in a sequence. Your calculation should be:

#percent GC content = 100 * (number of "C"s + number of "G"s) / (length of sequence)

from collections import defaultdict
import numpy as np
import random, re
#For info about the Binomial distribution
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html


#A = 1
#T = 2
#G = 3
#C = 4


def main():
	#n is the number of trials
	n = 30000
	#p is the probability of success
	p = random.uniform(0.01, 0.99)

	print 'Percent of GC in the sequence %s of out of %i bases' % (randomSeq(n, p), n)

def randomSeq(n, p):
	dnaSeq = np.random.binomial(4,  p, n)
	return "%.03f" % (100 * (np.count_nonzero(np.where(dnaSeq==3)) + np.count_nonzero(np.where(dnaSeq==4))) / float(len(dnaSeq)))

if __name__ == '__main__':
  main()
