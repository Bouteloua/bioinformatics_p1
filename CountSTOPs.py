import re
from collections import defaultdict
import numpy as np

#A = 1
#T = 2
#G = 3
#C = 4

def main():
	N = 30000
	randomDNA = randomSeq(N)

	print '%s:\t%s' % ('AAcid Code', 'Count')
	print '*' * 22

	for amino_code in set(randomDNA):
		print '%s:\t\t%s' % (amino_code, randomDNA.count(amino_code))

def randomSeq(N):
	NestedAminoDic = fileToDic()
	aminoAcidList = []
	dnaSeq = np.random.randint(1, 5, size=(N, 3))

	for codon in np.dot(dnaSeq, [100, 10, 1]):
		for amino, output_codons in NestedAminoDic.items():
			if codon in output_codons:
				aminoAcidList.append(amino)
	return aminoAcidList

def fileToDic():
	dataFile = open('aminonumber.csv')
	amicoDic = defaultdict(list)
	removeEndings = re.compile('[\r\n\t]')
	for index, line in enumerate(dataFile.readlines()):
		if index > 0:
			amicoDic[line.split(',')[0]].append(int(removeEndings.sub('', line.split(',')[1])))
	dataFile.close()
	return amicoDic

if __name__ == '__main__':
  main()
