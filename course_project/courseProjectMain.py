## CS 675 course project
## Binary classification of Simulated SNPs dataset
## Author: Haard Shah
## ucid: hks32

import sys

from sklearn import svm
from sklearn.naive_bayes import GaussianNB

from featureSelection import featureSelect, extractFeatures
from read_files import readLabels, readData

# from hinge_adaptive_eta import hingeAdaptive
# from least_squares_adaptive_eta import leastSquaredAdaptive

def extractTrainFromData(data, labels):
	trainData = []
	trainLabels = []
	for i, row in enumerate(data):
		if (labels.get(i) != None):
			trainData.append(row)
			trainLabels.append(labels[i])
	return trainData, trainLabels

def extractTestFromData(data, trainLabels):
	testData = []
	rowNumbers = []
	for i, row in enumerate(data):
		if (trainLabels.get(i) == None):
			testData.append(row)
			rowNumbers.append(i)
	return testData, rowNumbers

def calculateAccuracy(predictions, trueLabels):
	total = len(predictions)
	correct = 0

	for pred in predictions:
		if (pred[0] == trueLabels[pred[1]]):
			correct += 1

	accuracy = float(correct)/float(total)
	return accuracy

def calculateBalancedAccuracy(predictions, trueLabels):
	a = b = c = d = float(0.0)
	for pred in predictions:
		pval = pred[0]
		trueVal = trueLabels[pred[1]]
		if (pval == 0 and trueVal == 0):
			a += 1
		elif (pval == 1 and trueVal == 0):
			b += 1
		elif (pval == 0 and trueVal == 1):
			c += 1
		elif (pval == 1 and trueVal == 1):
			d += 1
	ber = 0.5*( (b / (a+b)) + (c / (c+d)) )
	accuracy = 1 - ber
	return accuracy

def printPredictions(predictions):
	for pred in predictions:
		print(pred[0], pred[1])

def convertScikitPredictionsToTuplePredictions(sciPredictions, rowNumbers):
	tuplePred = []
	for i in range(len(sciPredictions)):
		tuplePred.append((sciPredictions[i], rowNumbers[i]))
	return tuplePred

def runScikitSVM(newData, labels, C=1.0, verbose=False):
	# prepare data for sklearn.svm
	trainData, trainLabels = extractTrainFromData(newData, labels)
	# prepare test data for predictions later
	testData, rowNumbers = extractTestFromData(newData, labels)

	# run SVM
	if (verbose):
		print("Scikit learn svm training...", "C :", C)
	clf = svm.SVC(gamma='auto', C=1.0)
	clf.fit(trainData, trainLabels)

	# predict on testData
	sciPredictions = clf.predict(testData)

	# return predictions in tuple format [(label, row), ..., (label, row)]
	predictions = convertScikitPredictionsToTuplePredictions(sciPredictions, rowNumbers)
	return predictions

def runSciKitGaussianNaiveBayes(newData, labels, verbose=False):
	# prepare data for sklearn.svm
	trainData, trainLabels = extractTrainFromData(newData, labels)
	# prepare test data for predictions later
	testData, rowNumbers = extractTestFromData(newData, labels)

	# run Gaussian Naive Bayes
	if (verbose):
		print("Scikit learn gaussian naive bayes training...")
	gnb = GaussianNB()
	gnb.fit(trainData, trainLabels)

	# predict on testData
	sciPredictions = gnb.predict(testData)

	# return predictions in tuple format [(label, row), ..., (label, row)]
	predictions = convertScikitPredictionsToTuplePredictions(sciPredictions, rowNumbers)
	return predictions

def runAdapativeHinge(newData, labels, verbose=False):
	if (verbose):
		print("Adaptive hinge loss training...")
	predictions = hingeAdaptive(newData, labels)
	return predictions

def runAdaptiveLeastSquares(newData, labels, verbose=False):
	if (verbose):
		print("Adaptive least squares training...")
	predictions = leastSquaredAdaptive(newData, labels)
	return predictions

def run(data, labels, numFeatures, trueLabelsFile=None, verbose=False):
	if (trueLabelsFile != None):
		trueLabels = readLabels(trueLabelsFile)

	if (verbose):
		print("Selecting features...")
	# feature selection
	features = featureSelect(data, labels, numFeatures)
	# remove columns other than selected features
	newData = extractFeatures(data, features)

	C_vals = [0.001, 1.0, 1000]
	for C in C_vals:
		# run Scikit learn SVM
		predictions1 = runScikitSVM(newData, labels, C=C, verbose=verbose)
		# get accuracy
		if (trueLabelsFile != None):
			# accuracy = calculateAccuracy(predictions1, trueLabels)
			bAccuracy = calculateBalancedAccuracy(predictions1, trueLabels)
			if (verbose):
				# print("Accuracy:", accuracy)
				print("Balanced accuracy:", bAccuracy)

	# run Scikit naive bayes
	predictions4 = runSciKitGaussianNaiveBayes(newData, labels, verbose=verbose)
	# get accuracy
	if (trueLabelsFile != None):
		# accuracy = calculateAccuracy(predictions4, trueLabels)
		bAccuracy = calculateBalancedAccuracy(predictions4, trueLabels)
		if (verbose):
			# print("Accuracy:", accuracy)
			print("Balanced accuracy:", bAccuracy)

	# Not good accuracy
	# # run adaptive hinge svm
	# predictions2 = runAdapativeHinge(newData, labels, verbose=verbose)
	# if (trueLabelsFile != None):
	# 	accuracy = calculateAccuracy(predictions2, trueLabels)
	# 	if (verbose):
	# 		print("Accuracy:", accuracy)
	#
	# # run adaptive least squares
	# predictions3 = runAdaptiveLeastSquares(newData, labels, verbose=verbose)
	# if (trueLabelsFile != None):
	# 	accuracy = calculateAccuracy(predictions3, trueLabels)
	# 	if (verbose):
	# 		print("Accuracy:", accuracy)


def test():
	dataFile = "train_data/snps.data"
	trueLabelsFile = "train_data/snps.labels"
	labelsFilePrefix = "train_data/snps.trainlabels."

	data, rows, cols = readData(dataFile, verbose=True)
	listFeatures = [15, 30, 50]
	# listFeatures = [100, 500]

	numSplits = 10
	for numFeatures in listFeatures:
		for split in range(0, numSplits):
			labelsFile = labelsFilePrefix + str(split)
			labels = readLabels(labelsFile)
			print("----------Num features:", numFeatures, "----- Labels:", labelsFile, "----------")
			run(data, labels, numFeatures, trueLabelsFile=trueLabelsFile, verbose=True)

	exit()

def printTestPredictions(predictions, subtract):
	for pred in predictions:
		print(pred[0], pred[1]-subtract)

def bestClassifier(data, labels, numFeatures, trainDataSize=0):
	bestNumFeatures = None
	# feature selection
	features = featureSelect(data, labels, numFeatures)
	print("Feature column numbers:", features)
	# remove columns other than selected features
	newData = extractFeatures(data, features)

	predictions = runScikitSVM(newData, labels)

	printTestPredictions(predictions, trainDataSize)

if __name__ == "__main__":
	# test()

	if (len(sys.argv) != 4):
		print("Usage:", sys.argv[0], "<trainData> <labelsFile> <testData>")
		exit()

	dataFile = sys.argv[1]
	labelsFile = sys.argv[2]
	testFile = sys.argv[3] # for submission
	numFeatures = 15

	print("total number of features:", numFeatures)

	# read input data
	data, rows, cols = readData(dataFile)
	testData, _, _ = readData(testFile)
	labels = readLabels(labelsFile)

	combinedData = data + testData

	bestClassifier(combinedData, labels, numFeatures, trainDataSize=len(data))

















