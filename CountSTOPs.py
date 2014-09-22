#By: Brian Franzone
#Email: Franzone89@gmail.com
#For: Bioinformatics E-100. assignment 1 problem 3
#Summary: Ccalculates the ratio of all DNA Codons to Amino acids in a uniform, randomly generated sequence of integers.

#Detailed SUmmary:
#The main objective of this script is to use integers to practice generating sequences
#using numpy.  The script starts by generating a uniform, random sequence of integers. A = 1, T = 2, G = 3, C = 4. 
#By iterating through  all 3 codon frames, it looks up all the DNA codons to amino acid symbols. 
#How it accomplishes this: The script multiplies the Ones position by 1, tens position by 10, and the hundreds position by 100.
#This is how I am doing integer concatenation:
#A numpy slice will begin after the 1st (frame 1) iteration completes. 
#After the 2nd (frame 2) and 3rd (frame 3) iterations, it begins deleting index value [0][0] in the array, and 
#then inserting that into the last position of the array. The reason behind is that
#numpy array cannot be an uneven length. It has to be a length that is divisible by 3. 
#A file named "aminonumber.csv" will be used to create a dictionary. 
#This will return all the DNA codons to amino acids listed in http://en.wikipedia.org/wiki/DNA_codon_table. 
#After that point, it will send back to the main function and print out the count and percentage of each amino acid

#Base to int table
#A = 1
#T = 2
#G = 3
#C = 4

import numpy as np
import random

#The main function is to call the underlying functions: randomDnaSeqToAminoAcid, and to print out all the results.
def main():
	#N is the length of the randomly generated sequence
	N = 3000
	aminoAcids = randomDnaSeqToAminoAcid(N)
	print '%s:\t%s\t%s' % ('AAcid Code', 'Count', 'Percent')
	print '*' * 31

	#Count the total amount of amino acid 
	total = 0

	#Count the percent amount of amino acid
	percent = 0
	for aminoAcid in set(aminoAcids):
		total += aminoAcids.count(aminoAcid)
		percent += (aminoAcids.count(aminoAcid) / (N * 3.0) * 100.0)
		
		#Question three only requires to print out STOP codons. If you uncomment this section and the print statement, it will only print STOP codons.
		#if aminoAcid == 'STOP':
			#print '%s:\t\t%s\t %.02f' % (aminoAcid, aminoAcids.count(aminoAcid), (aminoAcids.count(aminoAcid) / float(N * 3.0) * 100.0))

		print '%s:\t\t%s\t %.02f' % (aminoAcid, aminoAcids.count(aminoAcid), (aminoAcids.count(aminoAcid) / float(N * 3.0) * 100.0))

	print '*' * 31
	print '%s:\t%s\t%.01f'% ('Total bases', total, percent) 

def randomDnaSeqToAminoAcid(N):
	#Calls the file that tranforms a file into a dictionary.
	aminoDictionary = fileToDic()

	#This is a placeholder to hold all 3 codon to amino acid frames.
	aminoLists = []

	#This is where a uniform, random integer sequence is generated.
	randomInt = np.random.randint(1, 5, size=(N, 3))

	#Iterates through all three codon frames to get all possible codon pairings.
	for index, frame in enumerate(xrange(3)):
		#If this the 1st iteration of the loop, this condition will be skipped because the data is already organized to run off the first codon sequence.
		#If this is the 2nd or 3rd run, begins deleting index value [0][0] in the array, and then inserting that into the last position of the array. 
		if index > 0:
			#deletes index value [0][0] and inserts that value in the last index value of the array 
			insertLastDelfirst = np.delete((np.insert(randomInt, np.size(randomInt), randomInt[0][0])), 0)

			#reshapes the arrary back to N by 3
			reshapeArrary = np.reshape(insertLastDelfirst, (np.size(insertLastDelfirst)/3, 3))

			#concatenates the arrary into the hundreds. Multiplies the Ones position by 1, tens position by 10, and the hundreds position by 100
			seqHunPos = np.dot(reshapeArrary, [100, 10, 1])

			#dictionary lookup from the variable named "aminoDictionary"
			aminoLists += [aminoDictionary[k] for k in seqHunPos]
		else:
			#concatenates the arrary into the hundreds. Multiplies the Ones position by 1, tens position by 10, and the hundreds position by 100
			seqHunPos = np.dot(randomInt, [100, 10, 1])

			#dictionary lookup from the variable named "aminoDictionary"
			aminoLists += [aminoDictionary[k] for k in seqHunPos] 
	return aminoLists

#Returns a dictionary of the file. Can create a lookup table of DNA codons -> Amino Acid 
def fileToDic():
	dataFile = open('DnaAminoTableFile/aminonumber.csv')
	amicoDic = {}
	for index, line in enumerate(dataFile.readlines()):
		if index > 0:
			#Returns the first column
			value = line.split(',')[0]

			#Returns the second column
			key = int(line.split(',')[1])

			#Key is DNA codons, Value is Amino Acids
			amicoDic[key] = value
			
#Closes the file
	dataFile.close()
	return amicoDic


if __name__ == '__main__':
  main()