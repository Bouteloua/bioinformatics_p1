#By: Brian Franzone
#Email: Franzone89@gmail.com
#For: Bioinformatics E-100. assignment 1 problem 1
#Summary: This script determines the total amount of GC content ratio in a given sequence. Ignores codon structures.


import random


def main():
	#N is the length of the randomly generated sequence
	N = 30000
	print 'GC content of sequence is: %s out of %i bases' % (ratioGC(N), N)

#This function first generates a random sequence, based off #N, and then calculates the percentage of GC in the sequence
def ratioGC(N):
	bases = "ACTG"
	seq = ""
	for i in xrange(N):
		seq += bases[random.randint(0,3)]
		
	#Pseudocode for the equation. GC content = 100 * (number of "C"s + number of "G"s) / (length of sequence)
	return "%.02f" % (100.0 * (seq.count('G') + seq.count('C')) / float(len(seq)))

if __name__ == '__main__':
	main()
