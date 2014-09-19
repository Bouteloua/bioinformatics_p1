import numpy as np
import random


#A = 1
#T = 2
#G = 3
#C = 4

def main():
	N = 300000
	P = random.uniform(0.01, 0.99)
	aminoAcid = randomSeq(N, P)
	print '%s:\t%s\t%s' % ('AAcid Code', 'Count', 'Percent')
	print '*' * 31

	total = 0
	percent = 0
	for amino_code in set(aminoAcid):
		total += aminoAcid.count(amino_code)
		percent += (aminoAcid.count(amino_code) / float(N) * 100.0)
		print '%s:\t\t%s\t%.02f p' % (amino_code, aminoAcid.count(amino_code), (aminoAcid.count(amino_code) / float(N) * 100.0))

	print '*' * 31
	print '%s:\t%s\t%.01f' % ('Total bases', total, percent) 

def randomSeq(N, P):
	NestedAminoDic = fileToDic()
	dnaSeq = np.dot(np.random.randint(1, 5, size=(N, 3)), [100, 10, 1])
	return [NestedAminoDic[k] for k in dnaSeq ]

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