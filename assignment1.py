## Naive Bayes binary classification Assignment
## CS675-001
## Author: Haard Shah
## Due date: Sept 23rd, 2018

import sys

###	Runs Naive Bayes Classifier on dataFile and trainingLabels. Then predicts class for nonlabeled points
##	returns test_pred[prediction class][sampleIndex]
def naive_classify(dataFile, trainingLabels):

	###	Read data from file
	datafile = dataFile
	f = open(datafile, 'r')
	data = []
	i = 0
	l = f.readline()
	while (l != ''):
	    a = l.split()
	    l2 = []
	    for j in range(len(a)):
	        l2.append(float(a[j]))
	    data.append(l2)
	    l = f.readline()

	rows = len(data)
	cols = len(data[0])
	f.close()

	###	Read lables
	labelfile = trainingLabels
	trainlabels = read_labels(labelfile)

	###	Compute means
	n = [0, 0]
	means = []
	means.append([])
	means.append([])
	std_dev = []
	std_dev.append([])
	std_dev.append([])
	for j in range(cols):
		means[0].append(1)
		means[1].append(1)
		std_dev[0].append(0)
		std_dev[1].append(0)

	for i in range(rows):
		if (trainlabels.get(i) != None):
			label = trainlabels[i]
			n[label] += 1
			for j in range(cols):
				means[label][j] = means[label][j] + data[i][j]

	for j in range(cols):
		means[0][j] = means[0][j] / n[0]
		means[1][j] = means[1][j] / n[1]

	###	Compute Standard Deviation
	#	std_dev = sqrt((1/N)*SUM(1->N)(xi-mean)**2)
	for i in range(rows):
		if (trainlabels.get(i) != None):
			label = trainlabels[i]
			for j in range(cols):
				std_dev[label][j] = std_dev[label][j] + (data[i][j] - means[label][j])**2
	for j in range(cols):
		for i in range(2): # two labels 0 and 1
			std_dev[i][j] = (std_dev[i][j] / n[i])**(.5)

	###	Classify unlabeled points
	test_pred = []
	for i in range(rows):
		if (trainlabels.get(i) == None):
			d = [0, 0]
			for j in range(cols):
				for k in range(2):
					d[k] = d[k] + ( (data[i][j] - means[k][j]) / std_dev[k][j] )**2
			if (d[0] < d[1]):	
				# print("0 ", i)
				test_pred.append([0, i])
			else:
				# print("1 ", i)
				test_pred.append([1, i])
	return test_pred

# returns trainlabels{datapoint : classification label}
def read_labels(file):
	f = open(file)
	trainlabels = {} # sample# : classification label
	l = f.readline()
	while (l != ''):
		a = l.split()
		trainlabels[int(a[1])] = int(a[0])
		l = f.readline()
	f.close()
	return trainlabels

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print("Usage:", sys.argv[0], "<datafile> <trainingLabels>")
		sys.exit(1)
	dataFile = sys.argv[1]
	trainingLabels = sys.argv[2]
	pred = naive_classify(dataFile, trainingLabels);
	for p in pred:
		print(p[0], p[1])




