import csv
import math


def loadData(fileName):
	''' Parses the csv file into a list of features '''

	with open(fileName) as handle:
		data = list(csv.reader(handle))
		data = data[1:] # remove the column names
		for row in range(len(data)):
			for col in range(14): # the minus one is to ignore the category
				data[row][col] = float(data[row][col])
	return data


def distance(x1,x2):
	''' Euclidian distance between two vectors of the same dimension'''

	# ignore the category. only want the feature vector
	if len(x1) == len(x2):
		x1 = x1[:-1]
	x2 = x2[:-1]

	return math.sqrt(sum((x-y)**2 for x, y in zip(x1,x2)))


def knn(k, data, testvector):
	''' Returns the k nearest neighbors that have the minimum distance to the testvector'''
	knn = []
	for trainvector in data:
		dist = distance(testvector, trainvector)
		knn.append((trainvector[-1], dist))
	knn.sort(key=lambda tup: tup[1])
	return knn[:k]


def tabulate_results(neighbors, predictions):
	''' Counts the labels of the k nearest neighbors and classifies the testvector with the majority '''

	mitt = 0
	barack = 0
	for neighbor in neighbors:
		name, dist = neighbor
		if name == "Barack Obama":
			barack += 1
		if name == "Mitt Romney":
			mitt += 1

	if mitt > barack:
		prediction = "Mitt Romney"
		count = mitt
	else:
		prediction = "Barack Obama"
		count = barack

	# print("Predicting " + prediction + " with a count of " + str(count))
	predictions.append(prediction)


def calculateAccuracy(predictions, testmatrix):
	''' Gives the percentage of the time knn algorithm got a prediction correct'''
	''' This was for testing purposes only, when I split up the training data to test accuracy '''
	correct = 0
	total = len(predictions)
	for i in range(len(testmatrix)):
		if predictions[i] == testmatrix[i][-1]:
			correct += 1
	return (correct / float(total)) * 100




if __name__=="__main__":

	data = loadData("train_potus_by_county.csv")
	testmatrix = loadData("test_potus_by_county.csv")

	predictions = []

	print "starting knn .."
	for testvector in testmatrix:
		neighbors = knn(10, data, testvector)
		tabulate_results(neighbors, predictions)
	print "done! prediction array returned "
	print predictions

	




		