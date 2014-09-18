#Program 1

#The amount of "GC content" is one of the signals that there is a gene present. http://en.wikipedia.org/wiki/GC-content#GC_ratio_of_genomes
#Write a small program called GCcontent.py to calculate the combined percentage of "C"s and "G"s in a sequence. Your calculation should be:

#percent GC content = 100 * (number of "C"s + number of "G"s) / (length of sequence)


import re
from collections import defaultdict
import numpy as np

#A = 1
#T = 2
#G = 3
#C = 4


def main():
	N = 3000000

	print 'Random DNA sequence content %s out of %i bases' % (randomSeq(N), N)

def randomSeq(N):
	dnaSeq = np.random.randint(1, 5, size=(N))
	return "%.03f" % (100 * (np.count_nonzero(np.where(dnaSeq==3)) + np.count_nonzero(np.where(dnaSeq==4))) / float(len(dnaSeq)))

if __name__ == '__main__':
  main()
