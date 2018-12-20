## Assignment7: Decision stump predictions
## CS675-001
## Author: Haard Shah
## Due date: Oct 7, 2018

import sys
from random import randint

from assignment6 import find_stump
# import math

def readData(dataFile):
	f = open(dataFile, 'r')
	data = []
	l = f.readline()
	while (l != ''):
		a = l.split()
		l2 = []
		for j in range(len(a)):
			l2.append(float(a[j]))
		# don't append dummy for decision stump
		# l2.append(1) # add dummy 1 at the end of x because of the w0 absorbed into w
		data.append(l2)
		l = f.readline()

	return (data, len(data), len(data[0])) # (2Ddata, rows, cols)

def readLabels(file):
	f = open(file)
	labels = {} # {sampleNum	:	classification label}
	l = f.readline()
	while (l != ''):
		a = l.split()
		labels[int(a[1])] = int(a[0])
		if (labels[int(a[1])] == 0):
			labels[int(a[1])] = -1
		l = f.readline()
	f.close()
	return labels 	# dict {sampleNum	:	classification label}

# return list of random row indices
def generateBootstrap(data, labels):
	n_rows = len(labels)
	keys_lst = list(labels.keys())
	boot_rows = [] # returning this 
	for i in range(n_rows):
		picked = randint(0, n_rows-1)
		boot_rows.append(keys_lst[picked])
	return boot_rows

def newDataLabels(oldData, labels):
	newdata = []
	newlabels = {}
	boot_idxes = generateBootstrap(oldData, labels)
	for i in range(len(boot_idxes)):
		tmp = boot_idxes[i]
		newdata.append(oldData[tmp])
		newlabels[i] = labels[tmp]
	return (newdata, newlabels)

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print("Usage:", sys.argv[0], "<dataFile> <trainlabels>")
		sys.exit(1)
	dataFile = sys.argv[1]
	trainlabels = sys.argv[2]

	data, rows, cols = readData(dataFile)
	trainlabels = readLabels(trainlabels)

	# print("ORIGINAL")
	# print(data)
	# print(trainlabels)

	nstraps = 100
	splits_lst = []
	for i in range(nstraps):
		# boot_idxes = generateBootstrap(data, trainlabels)
		newdata, newlabels = newDataLabels(data, trainlabels)
		# print("NEW", i)
		# print(newdata)
		# print(newlabels)
		best_k, best_split, left_label = find_stump(newdata, newlabels, debug_print=False)
		if (best_k == "error"):
			continue
		# print("stump:")
		# print(best_k, best_split, left_label)
		splits_lst.append((best_k, best_split, left_label))

	# print(splits_lst)
	# now predict from orig data and trainlabels
	predictions_dict = {}
	for i in range(rows):
		if (trainlabels.get(i) == None):
			zeros = ones = 0
			for split in splits_lst:
				left_label = split[2]
				best_k = split[0]
				best_split = split[1]
				if (data[i][best_k] < best_split):
					if (left_label == 0):
						zeros += 1
					else:
						ones += 1
				elif (data[i][best_k] > best_split):
					if (left_label == 0):
						ones += 1
					else:
						zeros += 1
			predictions_dict[i] = [zeros, ones] # not using but maybe for record keeping later or if turned into a function return this
			if (zeros > ones):
				print("0", i)
			else:
				print("1", i)

	# if not stumps were created because of invalid input data it will predict 1 everytime but state the error
	if not splits_lst:
		print("ERROR:", "Repetative Data - STUMPS COULD NOT BE CREATED")



















