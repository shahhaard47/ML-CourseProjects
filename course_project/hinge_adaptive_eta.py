## Assignment 5
## Hinge loss gradient descent with adaptive eta
## CS675-001
## Author: Haard Shah
## Due date: Nov 5, 2018

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
		l2.append(1) # add dummy 1 at the end of x because of the w0 absorbed into w
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

def objective(labels, data, w):
	obj = 0
	for i in range(len(data)):
		if (labels.get(i) != None):
			obj += max(0, 1 - labels[i] * dot(w, data[i]))
	return obj

def hingeAdaptive(dataFile, labelsFile):
	# data, rows, cols = readData(dataFile)
	# trainlabels = readLabels(labelsFile)
	# MODIFIED FOR COURSE PROJ
	data = dataFile
	rows = len(data)
	cols = len(data[0])
	trainlabels = labelsFile

	## Initialize random w
	w = [0.02*random()-0.01 for _ in range(cols)]

	## Gradient Descent
	# eta = 0.001
	# eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
	eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001, .000000000001, .0000000000001, .00000000000001, .000000000000001, .0000000000000001, .00000000000000001 ]
	best_eta = 1
	# stop_cond = 0.0001
	stop_cond = 0.00001
	iter = 0
	prev_error = 100000000 #arbitrary big error
	converged = False
	best_obj = 1000000000000
	while not converged: 

		prev_error = best_obj
		# Compute dellF
		dellF = [0 for _ in range(cols)]
		for i in range(rows):
			if (trainlabels.get(i) != None):
				dotprod = dot(w, data[i])
				for j in range(cols):
					if ((dotprod)*trainlabels[i] < 1):
						dellF[j] += data[i][j]*trainlabels[i]
					else:
						dellF[j] += 0

		# ADAPTIVE loops
		for eta in eta_list:
			## update w
			for j in range(cols):
				w[j] = w[j] + eta*dellF[j]

			## compute error: least squares
			error = objective(trainlabels, data, w);

			##update best_obj and best_eta
			if (error < best_obj):
				best_obj = error
				best_eta = eta

			##remove the eta for the next
			for j in range(cols):
				w[j] = w[j] - eta*dellF[j]

		#final update for w
		eta = best_eta
		for j in range(cols):
			w[j] = w[j] + eta*dellF[j]

		diff = abs(prev_error - best_obj)
		# prev_error = best_obj
		if (diff < stop_cond):
			converged = True
		# print(iter, "Objective:", best_obj, "\teta:", best_eta)
		iter += 1

	# print("w:", w[:-1])
	# print("w0:", w[cols-1])
	w_norm = 0
	for j in range(cols-1):
		w_norm += w[j]**2
	w_norm = w_norm**0.5
	d_origin = w[len(w)-1]/w_norm;
	d_origin = abs(d_origin);
	# print("||w||:", w_norm)
	# print("Distance to origin:", d_origin)

	## Predict unlabeled points
	predictions = []
	for i in range(rows):
		if (trainlabels.get(i) == None):
			if (dot(w, data[i]) > 0):
				predictions.append((1, i))
				# print("1 ", i)
			else:
				predictions.append((0, i))
				# print("0 ", i)
	return predictions

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print("Usage:", sys.argv[0], "<dataFile> <trainingLabels>")
		sys.exit(1)
	dataFile = sys.argv[1]
	trainingLabels = sys.argv[2]

	predictions = hingeAdaptive(dataFile, trainingLabels)

	for pred in predictions:
		print(pred[0], pred[1])

	# data, rows, cols = readData(dataFile)
	# trainlabels = readLabels(trainingLabels)

	# ## Initialize random w
	# w = [0.02*random()-0.01 for _ in range(cols)]

	# ## Gradient Descent
	# # eta = 0.001
	# eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
	# # eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001, .000000000001, .0000000000001, .00000000000001, .000000000000001, .0000000000000001, .00000000000000001 ]
	# best_eta = 1
	# # stop_cond = 0.0001
	# stop_cond = 0.001
	# iter = 0
	# prev_error = 100000000 #arbitrary big error
	# converged = False
	# best_obj = 1000000000000
	# while not converged: 

	# 	prev_error = best_obj
	# 	# Compute dellF
	# 	dellF = [0 for _ in range(cols)]
	# 	for i in range(rows):
	# 		if (trainlabels.get(i) != None):
	# 			dotprod = dot(w, data[i])
	# 			for j in range(cols):
	# 				if ((dotprod)*trainlabels[i] < 1):
	# 					dellF[j] += data[i][j]*trainlabels[i]
	# 				else:
	# 					dellF[j] += 0

	# 	# ADAPTIVE loops
	# 	for eta in eta_list:
	# 		## update w
	# 		for j in range(cols):
	# 			w[j] = w[j] + eta*dellF[j]

	# 		## compute error: least squares
	# 		error = objective(trainlabels, data, w);

	# 		##update best_obj and best_eta
	# 		if (error < best_obj):
	# 			best_obj = error
	# 			best_eta = eta

	# 		##remove the eta for the next
	# 		for j in range(cols):
	# 			w[j] = w[j] - eta*dellF[j]

	# 	#final update for w
	# 	eta = best_eta
	# 	for j in range(cols):
	# 		w[j] = w[j] + eta*dellF[j]

	# 	diff = abs(prev_error - best_obj)
	# 	# prev_error = best_obj
	# 	if (diff < stop_cond):
	# 		converged = True
	# 	# print(iter, "Objective:", best_obj, "\teta:", best_eta)
	# 	iter += 1

	# # print("w:", w[:-1])
	# # print("w0:", w[cols-1])
	# w_norm = 0
	# for j in range(cols-1):
	# 	w_norm += w[j]**2
	# w_norm = w_norm**0.5
	# d_origin = w[len(w)-1]/w_norm;
	# d_origin = abs(d_origin);
	# # print("||w||:", w_norm)
	# # print("Distance to origin:", d_origin)

	# ## Predict unlabeled points
	# for i in range(rows):
	# 	if (trainlabels.get(i) == None):
	# 		if (dot(w, data[i]) > 0):
	# 			print("1 ", i)
	# 		else:
	# 			print("0 ", i)









