#By: Brian Franzone
#Email: Franzone89@gmail.com
#For: Bioinformatics E-100. assignment 1 problem 3
#Count the number of all DNA Codons to Amino acid in a given sequence.
#Used this DNA codon table:
	#http://en.wikipedia.org/wiki/DNA_codon_table
# Not sure what is the diffences between START ATG and Met/M ATG so it is just all set to Start
# Note: Trying to learn a different way of doing it but in the it's not that fast but learned alot more about numpy functions.
# Some of this script is reductant 
# Need to think the design out more before I start wrting.

#Base to int table
#A = 1
#T = 2
#G = 3
#C = 4

import numpy as np
import random

def main():
	# Number of random DNA bases
	N = 3000
	aminoAcid = randomSeqToAmino(N)
	print '%s:\t%s\t%s' % ('AAcid Code', 'Count', 'Percent')
	print '*' * 31

	total = 0
	percent = 0
	for amino_code in set(aminoAcid):
		total += aminoAcid.count(amino_code)
		percent += (aminoAcid.count(amino_code) / (N * 3.0) * 100.0)
		print '%s:\t\t%s\t %.02f' % (amino_code, aminoAcid.count(amino_code), (aminoAcid.count(amino_code) / float(N * 3.0) * 100.0))

	print '*' * 31
	print '%s:\t%s\t%.01f'% ('Total bases', total, percent) 

def randomSeqToAmino(N):
	#Calls the function
	NestedAminoDic = fileToDic()
	#Hold the concatenation of the three iteration of all linear possible condon pairing
	AminoList = []
	#Int generator of random DNA sequence
	randomInt = np.random.randint(1, 5, size=(N, 3))
	#iteration three times to get all possible condon pairings
	for index, i in enumerate(xrange(3)):
		#Skip first iteration before deleting  zero index value and inserting into the last 
		#index value so can found all possible condon pairing can be found 
		if index > 0:
			insertLastDelfirst = np.delete((np.insert(randomInt, np.size(randomInt), i)), 0)
			reshapeArrary = np.reshape(insertLastDelfirst, (np.size(insertLastDelfirst)/3, 3))
			dnaSeq = np.dot(reshapeArrary, [100, 10, 1])
			AminoList += [NestedAminoDic[k] for k in dnaSeq ]
		else:
			dnaSeq = np.dot(randomInt, [100, 10, 1])
			AminoList += [NestedAminoDic[k] for k in dnaSeq ] 
	return AminoList

def fileToDic():
	dataFile = open('aminonumber.csv')
	amicoDic = {}
	for index, line in enumerate(dataFile.readlines()):
		if index > 0:
			value = line.split(',')[0]
			key = int(line.split(',')[1])
			amicoDic[key] = value
	dataFile.close()
	return amicoDic


if __name__ == '__main__':
  main()