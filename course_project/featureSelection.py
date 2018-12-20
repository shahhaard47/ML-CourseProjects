# used by courseProject.py
# Feature selection

def chiSquared(data, labels, top):
	rows = len(data)
	cols = len(data[0])
	T = []
	for j in range(0, cols):
		ct = [[1,1],[1,1],[1,1]]    # contingency table
		for i in range(0, rows):
			if (labels.get(i) != None):
				if (labels[i] == 0):
					if (data[i][j] == 0):
						ct[0][0] += 1
					elif (data[i][j] == 1):
						ct[1][0] += 1
					elif (data[i][j] == 2):
						ct[2][0] += 1
				elif (labels[i] == 1):
					if (data[i][j] == 0):
						ct[0][1] += 1
					elif (data[i][j] == 1):
						ct[1][1] += 1
					elif (data[i][j] == 2):
						ct[2][1] += 1
		col_totals = [ sum(x) for x in ct]
		row_totals = [ sum(x) for x in zip(*ct) ]
		total = sum(col_totals)
		exp_value = [[(row*col)/total for row in row_totals] for col in col_totals]
		sqr_value = [[((ct[i][j] - exp_value[i][j])**2)/exp_value[i][j] for j in range(0,len(exp_value[0]))] for i in range(0,len(exp_value))]
		x_2 = sum([sum(x) for x in zip(*sqr_value)])
		T.append(x_2)
	indices = sorted(range(len(T)), key=T.__getitem__, reverse=True)
	idx = indices[:top]
	return idx

# def pearsonCoeff(data, labels, top):

def featureSelect(data, trainLabels, numFeatures):
	features = chiSquared(data, trainLabels, numFeatures)
	return features

def extractFeatures(data, features):
	newData = []
	for row in data:
		tmpRow = []
		for f in features:
			tmpRow.append(row[f])
		newData.append(tmpRow)
	return newData










