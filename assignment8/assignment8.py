## Assignment8: K-means clustering algorithm implementation
## CS675-001
## Author: Haard Shah
## Due date: Nov 19, 2018

import sys
import random
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
        # don't append dummy for kmeans
        # l2.append(1) # add dummy 1 at the end of x because of the w0 absorbed into w
        data.append(l2)
        l = f.readline()

    return (data, len(data), len(data[0])) # (2Ddata, rows, cols)

# ||xi - m||^2
def findSquaredDist(dataPoint, mean):
    if (len(dataPoint) != len(mean)):
        print("Error: Dimension of dataPoint and mean don't match.")
        return 0
    distance = 0
    for i, elem in enumerate(dataPoint):
        distance += (elem - mean[i])**2
    return distance

# ||xi - m||
def findDist(dataPoint, mean):
    distance = findSquaredDist(dataPoint, mean)
    return math.sqrt(distance)

# mean for C = sum(all x in C)/|C|
def computeMeans(data, labels, k):
    # ASSUME len(data) != 0
    numCols = len(data[0])
    means = [[0 for _ in range(numCols)] for _ in range(k)]

    clusterSizes = [0 for _ in range(k)]

    for i, dataPoint in enumerate(data):
        cluster = labels[i]
        clusterSizes[cluster] += 1

        for j, value in enumerate(dataPoint):
            means[cluster][j] += value

    # divide by clusterSizes
    for i in range(k):
        csize = clusterSizes[i]
        if (csize == 0):
            continue
        for j in range(numCols):
            means[i][j] /= csize

    return means

def recomputeClusters(data, labels, means):
    k = len(means)
    newLabels = {}

    for i, dataPoint in enumerate(data):
        origCluster = labels[i]
        minDist = findDist(dataPoint, means[origCluster])
        minCluster = origCluster

        for j in range(k):
            if (j == origCluster):
                continue
            tmpDist = findDist(dataPoint, means[j])
            if (tmpDist < minDist):
                minDist = tmpDist
                minCluster = j

        if (minCluster != origCluster):
            labels[i] = minCluster
    return labels

def objective(data, labels, means):
    obj = 0
    for i, dataPoint in enumerate(data):
        mean = means[labels[i]]
        obj += findSquaredDist(dataPoint, mean)
    return obj

if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print("Usage:", sys.argv[0], "<dataFile> <k-clusters>")
        sys.exit(1)

    dataFile = sys.argv[1]
    k = sys.argv[2]
    k = int(k)

    data, rows, cols = readData(dataFile)

    labels = {}

    # 1. initialize assign data to random clusters
    for i, dataPoint in enumerate(data):
        picked_class = random.randint(0, k-1)
        labels[i] = picked_class

    # compute means
    means = computeMeans(data, labels, k)

    prevObj = objective(data, labels, means)
    print("initial obj", prevObj)

    converged = False
    stoppingCondition = 0.001

    iter = 0
    while not converged:
        iter += 1
        labels = recomputeClusters(data, labels, means)
        means = computeMeans(data, labels, k)
        obj = objective(data, labels, means)

        print(iter, "obj", obj)

        if ((prevObj - obj) < stoppingCondition):
            converged = True
        prevObj = obj


    # output labels
    for i, dataPoint in enumerate(data):
        print(labels[i], "\t", i)























