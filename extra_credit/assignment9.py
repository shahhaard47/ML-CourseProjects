##################################
##  Extra credit Assignment 9
##  Random Hyperplanes
##  Author: Haard Shah
##################################

import sys
from read_files import readData, readLabels
from random import random
from sklearn import svm
from sklearn.metrics import accuracy_score

# predict wj between -1 and 1
def generateW(cols):
	w = [random()*2-1 for _ in range(cols)]
	return w

def dot(xj, w):
	if (len(xj) != len(w)): #sanity check
		print("Error: dimensionality mismatch - number of features must equal number of weights.")
		exit(1)
	prod = 0
	for i in range(len(xj)):
		prod += xj[i] * w[i]

	return prod

def sign(num):
	# print((num>=0) - (num<0))
	return (num>=0) - (num<0)

def calculateZ(X, w, labels):
	zi = []
	initial = True
	for i, x in enumerate(X):
		tmp = dot(x, w)
		zi.append(tmp)
		if (labels.get(i) != None): # use only train data to pick w0
			if (initial):
				mindot = maxdot = tmp
				initial = False
			else:
				if (tmp < mindot):
					mindot = tmp
				if (tmp > maxdot):
					maxdot = tmp
	rangedot = maxdot - mindot
	w0 = random()*rangedot + mindot

	# print(zi)

	zi_final = [(1+sign(val+w0))/2 for val in zi]

	# print(zi_final)

	return zi_final

def splitData(Z, labels):
	trainData = []
	trainLabels = []
	testData = []
	testDataOriginalRowNums = []
	for i in range(len(Z)):
		if (labels.get(i) != None):
			trainData.append(Z[i])
			trainLabels.append(labels[i])
		else:
			testData.append(Z[i])
			testDataOriginalRowNums.append(i)

	return (trainData, trainLabels, testData, testDataOriginalRowNums)

def convertScikitPredictionsToTuplePredictions(sciPredictions, rowNumbers):
	tuplePred = []
	for i in range(len(sciPredictions)):
		tuplePred.append((sciPredictions[i], rowNumbers[i]))
	return tuplePred

def regularSVM(data, labels, C=1.0, verbose=False, printTrainAccuracy=False):
	if (verbose):
		print("----------------- Regular SVM -----------------")
	rows = len(data)
	cols = len(data[0])

	if (verbose):
		print("Preparing training data...")
	trainData, trainLabels, testData, testDataOrigRowNums = splitData(data, labels)

	if (verbose):
		print("Training SciKit learn SVM...")
	clf = svm.SVC(gamma='auto', C=C, max_iter=-1, verbose=verbose)
	clf.fit(trainData, trainLabels)

	tmpPreds = clf.predict(trainData)
	cv_acc = accuracy_score(trainLabels, tmpPreds)
	if (printTrainAccuracy):
		print("Train complete, accuracy =", cv_acc)

	if (verbose):
		print("Predicting testlabels...")
	sciPredictions = clf.predict(testData)

	predictions = convertScikitPredictionsToTuplePredictions(sciPredictions, testDataOrigRowNums)
	return predictions, 1-cv_acc


def randomHyperplanes(data, labels, k_val, C=1.0, verbose=False, printTrainAccuracy=False):
	if (verbose):
		print("----------------- SVM with Random Hyperplanes -----------------")
	rows = len(data)
	cols = len(data[0])

	Z = [[0 for y in range(k_val)] for x in range(rows)]
	newRows = len(Z)
	newCols = len(Z[0])

	if (verbose):
		print("Generating random hyperplanes...")
	#   calculate Z
	for k in range(k_val):
		w = generateW(cols)
		zi = calculateZ(data, w, labels)
		for i in range(len(zi)):
			Z[i][k] = zi[i]
	# exit()

	if (verbose):
		print("Preparing training data...")
	#   separate into traindata, trainlabels, testdata
	trainData, trainLabels, testData, testDataOrigRowNums = splitData(Z, labels)

	if (verbose):
		print("Training Scikit learn SVM...")
	#   using sklearn svm
	clf = svm.SVC(gamma='auto', C=C, max_iter=-1, verbose=verbose)
	clf.fit(trainData, trainLabels)

	tmpPreds = clf.predict(trainData)
	cv_acc = accuracy_score(trainLabels, tmpPreds)
	if (printTrainAccuracy):
		print("Train complete, accuracy =", cv_acc)

	if (verbose):
		print("Predicting labels on test data...")
	#   predict labels on testData
	sciPredictions = clf.predict(testData)

	predictions = convertScikitPredictionsToTuplePredictions(sciPredictions, testDataOrigRowNums)
	return predictions, 1-cv_acc

def printPredictions(predictions):
	for pred in predictions:
		print(pred[0], pred[1])

if __name__ == '__main__':

	if (len(sys.argv) != 4):
		print("Usage:", sys.argv[0], "<dataFile> <trainLabelsFile> <k>")
		exit(1)

	dataFile = sys.argv[1]
	labelsFile = sys.argv[2]
	k_val = int(sys.argv[3])

	data, _, _ = readData(dataFile)
	labels = readLabels(labelsFile)

	predictions = randomHyperplanes(data, labels, k_val, verbose=True, printTrainAccuracy=False)

	printPredictions(predictions)










