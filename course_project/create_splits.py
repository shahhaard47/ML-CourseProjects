## CS 675 Course project
## Author: Haard Shah

from read_files import readData, readLabels
import sys
import os
import random

# hello OYOOOO

TRAIN_FOLDER = "train_data"
DATA_NAME = ""
TRAIN_PATH = os.path.join(os.getcwd(), TRAIN_FOLDER)
OUTPUT_TRAIN_PREFIX = ""

def createTrainDir():
	if not os.path.exists(TRAIN_PATH):
		os.makedirs(TRAIN_PATH)

# range (0, 1)
# returns a list of numbers between [0, numLabels) and size < numLabels*percentage
def split(percent, numLabels):
	allRows = [i for i in range(numLabels)]
	random.shuffle(allRows)
	allRows = allRows[:int(numLabels*percent)]
	return allRows

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		print("Usage:", sys.argv[0], "<labelsFile> <numSplits>")
		exit()

	createTrainDir()

	labelFile = sys.argv[1]
	numSplits = int(sys.argv[2])

	DATA_NAME = labelFile.split('.')[0]
	OUTPUT_TRAIN_PREFIX = DATA_NAME + ".trainlabels."

	splitPercent = 0.80 # 80 train 20 validation

	allLabels = readLabels(labelFile)
	numLabels = len(allLabels)

	for i in range(numSplits):
		newSplit = split(splitPercent, numLabels)
		outputFileName = OUTPUT_TRAIN_PREFIX + str(i)
		f = open(outputFileName, 'w')
		for key in newSplit:
			f.write(str(allLabels[key]) + " " + str(key) + "\n")
		f.close()








