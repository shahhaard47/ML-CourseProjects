##################################
##  Extra credit Assignment 9
##  Random Hyperplanes Calculating error
##  Author: Haard Shah
##################################


import sys
from assignment9 import randomHyperplanes, regularSVM
from read_files import readData, readLabels

def calculateBalancedError(predictions, trueLabels):
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
	return ber


if (len(sys.argv) != 2):
	print("Usage:", sys.argv[0], "<datasetName|all>")
	exit()

numSplits = 1
# k_vals = [10, 100, 1000, 10000]
k_vals = [10000]

argument = sys.argv[1]
if (argument == 'all'):
	# datasets = ['ionosphere', 'breast_cancer', 'qsar', 'climate', 'micromass', 'hill_valley']
	datasets = ['micromass', 'hill_valley']
else:
	datasets = [argument]

for k in k_vals:
	for datasetName in datasets:
		base = '../datasets/' + datasetName + '/'
		train_base = base + datasetName + '.trainlabels.'

		dataFile = base + datasetName + '.data'
		trueLabelsFile = base + datasetName + '.labels'

		# read true labels
		trueLabels = readLabels(trueLabelsFile)

		C_vals = [0.001, 0.01, 0.1, 1, 10, 100]

		#   read data
		data, _, _ = readData(dataFile)

		for split in range(numSplits):
			print("----------------------------------------------")
			print(datasetName, "split", split)
			labelsFile = train_base + str(split)
			#   read labels
			labels = readLabels(labelsFile)

			initial = True
			#   run regular SVM
			for C in C_vals:
				predictions, cv_err = regularSVM(data, labels, C=C, verbose=True)
				test_err = calculateBalancedError(predictions, trueLabels)
				if (initial):
					initial = False
					best_C = C
					best_cv_err = cv_err
					best_test_err = test_err
				else:
					if (test_err < best_test_err):
						best_C = C
						best_cv_err = cv_err
						best_test_err = test_err
			print("Original data: LinearSVC best C =", best_C, ", test error =", best_test_err * 100, "%")

			initial = True
			#   run random hyperplanes
			for C in C_vals:
				predictions, cv_err = randomHyperplanes(data, labels, k, C=C, verbose=True)
				test_err = calculateBalancedError(predictions, trueLabels)
				if (initial):
					initial = False
					best_C = C
					best_cv_err = cv_err
					best_test_err = test_err
				else:
					if (test_err < best_test_err):
						best_C = C
						best_cv_err = cv_err
						best_test_err = test_err
			print("Random hyperplanes data:")
			print("For k=", k)
			print("LinearSVC best C =", best_C, ", test error =", best_test_err * 100, "%")
	print("++++++++++++++++++++++++++++++++++++++++++++++")









