## Gradient descent binary classification Assignment 2
## CS675-001
## Author: Haard Shah
## Due date: Oct 1, 2018

import sys
from random import random

def readData(dataFile):
	f = open(dataFile, 'r')
	data = []
	l = f.readline()
	while (l != ''):
		a = l.split()
		l2 = []
		for j in range(len(a)):
			l2.append(float(a[j]))
		l2.append(1)
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

def dot(w, x):
	dotprod = 0
	for i in range(len(w)): #both sould have same len
		dotprod += w[i] * x[i]
	return dotprod

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print("Usage:", sys.argv[0], "<dataFile> <trainingLabels>")
		sys.exit(1)
	dataFile = sys.argv[1]
	trainingLabels = sys.argv[2]

	data, rows, cols = readData(dataFile)
	trainlabels = readLabels(trainingLabels)

	## Initialize random w
	w = [0.02*random()-0.01 for _ in range(cols)]

	## Gradient Descent
	eta = 0.0001
	stop_cond = 0.001
	diff = 100
	prev_error = 1000 #arbitrary big error
	while (diff > stop_cond): 

		# Compute dellF
		dellF = [0 for _ in range(cols)]
		for i in range(rows):
			if (trainlabels.get(i) != None):
				dotprod = dot(w, data[i])
				for j in range(cols):
					dellF[j] += (trainlabels[i] - dotprod)*data[i][j]

		## update w
		for j in range(cols):
			w[j] = w[j] + eta*dellF[j]

		## compute error
		error = 0;
		for i in range(rows):
			if (trainlabels.get(i) != None):
				error += (trainlabels[i] - dot(w, data[i]))**2;

		diff = abs(prev_error - error)
		prev_error = error
		print("error:", error, "\tdiff:", diff)

	print("w:", w[:-1])
	w_norm = 0
	for j in range(cols-1):
		w_norm += w[j]**2
	w_norm = w_norm**0.5
	d_origin = w[len(w)-1]/w_norm;
	d_origin = abs(d_origin);
	print("||w||:", w_norm)
	print("Distance to origin:", d_origin)

	## Predict unlabeled points
	for i in range(rows):
		if (trainlabels.get(i) == None):
			if (dot(w, data[i]) > 0):
				print("1 ", i)
			else:
				print("0 ", i)









