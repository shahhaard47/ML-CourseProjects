## Assignment6: Decision stump
## CS675-001
## Author: Haard Shah
## Due date: Oct 7, 2018

import sys
from random import random
import math

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

def column(matrix, col):
	return [row[col] for row in matrix]

def gini_function(lsize, rsize, lp, rp, numrows):
	g = lp*(1-lp)/(numrows*lsize) + rp*(1-rp)/(numrows*rsize)
	return g

def find_gini(stump, colnum, data, trainlabels):
	lsize = rsize = lp = rp = float(0)
	numrows = len(data)
	for i in range(numrows):
		if (trainlabels.get(i) != None):
			if (data[i][colnum] < stump):
				lsize += 1
				if (trainlabels[i] == -1):
					lp += 1
			else:
				rsize += 1
				if (trainlabels[i] == -1):
					rp += 1
	return gini_function(lsize, rsize, lp, rp, numrows)

## FIX in assignment 6: should only compute stumps between datapoints for which labels are available
def find_stump(data, trainlabels, debug_print=False):
	colstumpgini_dict = {} # col : (stump, gini)
	
	# this traindata will only be used just to calculate stumps between the train data points
	# therefore row #s of traindata won't and don't need to correspond to the row numbers of 
	#	original data and trainlables
	traindata = []
	if (len(data) != len(trainlabels)):
		# extract train data depending on which labels are available
		for i in range(len(data)):
			if (trainlabels.get(i) != None):
				traindata.append(data[i])
	else:
		traindata = data
	cols = len(data[0]) # data can't be empty ASSUME
	for col in range(cols):
		currcol = column(traindata, col)
		currcol.sort()
		# print(currcol)
		stumpgini_dict = {} # stump : gini
		for i in range(len(currcol)-1):
			if (currcol[i] == currcol[i+1]):
				continue
			#	Find stump
			# should be positive because currcol is sorted
			stump = currcol[i] + (currcol[i+1] - currcol[i]) / 2.0
			# get gini
			# **its important to pass in "data" and not traindata inside find_gini
			#	because its relying indexes of "data" as row# keys for trainlables
			gini = find_gini(stump, col, data, trainlabels)
			# add to dictionary
			stumpgini_dict[stump] = gini
		
		# add stump with min gini to colstumpgini_dict
		if (len(stumpgini_dict) == 0):
			continue
		best_stump = min(stumpgini_dict, key=stumpgini_dict.get)
		colstumpgini_dict[col] = (best_stump, stumpgini_dict[best_stump]) 

	# for key in colstumpgini_dict:
	# 	print(key, colstumpgini_dict[key])
	if (debug_print):
		if (len(colstumpgini_dict) == 0):
			# print unique data points (because stumps are created between points; if points are not unique then no stumps were probably created)
			print("Error:", "NO STUMPS WERE CREATED...")
			print("Data:", data)
			print("Labels:", trainlabels)
			exit()
	if (not len(colstumpgini_dict)): # non unique data
		return ("error", "error")
	# find col with minimum 
	# SOF: https://stackoverflow.com/questions/6349296/sorting-a-dict-with-tuples-as-values
	best_k = sorted(colstumpgini_dict.keys(), key=lambda x: colstumpgini_dict[x][1], reverse=False)
	best_k = best_k[0] ## FIX ME: IndexError: list index out of range
	best_stump = colstumpgini_dict[best_k][0]
	# print("BEST_K",best_k, "BEST STUMP", best_stump)

	return (best_k, best_stump)

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print("Usage:", sys.argv[0], "<dataFile> <trainingLabels>")
		sys.exit(1)
	dataFile = sys.argv[1]
	trainingLabels = sys.argv[2]

	data, rows, cols = readData(dataFile)
	trainlabels = readLabels(trainingLabels)

	best_k, best_stump = find_stump(data, trainlabels)
	print("K =", best_k, ";\ts =", best_stump)











