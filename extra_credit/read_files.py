## CS 675 Course project
## Author: Haard Shah

from array import array

# does not split lines into columns
def readDataLines(dataFile):
	f = open(dataFile, 'r')
	data = []
	l = f.readline()
	while (l != ''):
		data.append(l)
		l = f.readline()
	return (data, len(data)) # (dataLines, rows)

def readData(dataFile, verbose=False):
	f = open(dataFile, 'r')
	data = []
	l = f.readline()
	iter = 0
	while (l != ''):
		a = l.split()
		l2 = []
		for j in range(len(a)):
			l2.append(float(a[j]))
		# don't append dummy for kmeans
		# l2.append(1) # add dummy 1 at the end of x because of the w0 absorbed into w
		data.append(l2)
		l = f.readline()
		iter += 1
		if (verbose):
			if (iter % 1000 == 0):
				print("Reading data: current iter -", iter)

	return (data, len(data), len(data[0])) # (2Ddata, rows, cols)

# for the SNP high dimensional data
#   but didn't end up using this because (OSL machine had no problem with the dataset)
def readSnpDataArray(dataFile, verbose=False):
	f = open(dataFile, 'r')
	data = []
	l = f.readline()
	iter = 0
	while (l != ''):
		a = l.split()
		l2 = array('i')
		for j in range(len(a)):
			l2.append(int(a[j]))
		data.append(l2)
		l = f.readline()
		iter += 1
		if (verbose):
			if (iter % 1000 == 0):
				print("Reading data: current iter -", iter)
	return (data, len(data), len(data[0]))

def readLabels(file):
	f = open(file)
	labels = {} # {sampleNum    :   classification label}
	l = f.readline()
	while (l != ''):
		a = l.split()
		labels[int(a[1])] = int(a[0])
		# if (labels[int(a[1])] == 0):
		#     labels[int(a[1])] = -1
		l = f.readline()
	f.close()
	return labels   # dict {sampleNum   :   classification label}