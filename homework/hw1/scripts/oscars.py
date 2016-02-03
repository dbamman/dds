import sys,re
import numpy as np
from sklearn import linear_model,cross_validation
from sklearn import grid_search

from scipy import sparse

featureIds={}
docIds={}
goldVals={}
F=0
D=0
testId=0
X=None
Y=None
X_test=None
testNames=None
logreg=None

testData={}
goldNames=[]


def readData(filename):
	global X, Y, D, F, X_test
	maxFeat=0
	maxDocId=0

	with open(filename) as file:
		for line in file:
			cols=line.rstrip().split("\t")
			featureName=cols[0]
			docId=cols[2]

			# only consider features for movies/actors in the training/test data
			if docId not in docIds and docId not in testData:
				continue

			if featureName not in featureIds:
				featureIds[featureName]=maxFeat
				maxFeat+=1

	F=maxFeat

	X = sparse.lil_matrix((D, maxFeat))	# create documents x features empty sparse matrix
	X_test = sparse.lil_matrix((testId, maxFeat))	# create documents x features empty sparse matrix
	
	Y = np.zeros(D)
	for docId in docIds:
		Y[docIds[docId]]=goldVals[docIds[docId]]

	with open(filename) as file:
		for line in file:
			cols=line.rstrip().split("\t")
			featureName=featureIds[cols[0]]

			featureValue=float(cols[1])

			if cols[2] in docIds:
				docId=docIds[cols[2]]
				X[docId, featureName]=featureValue

			elif cols[2] in testData:
				docId=testData[cols[2]]
				X_test[docId, featureName]=featureValue


def readGold(filename, earliestDate, predictionYear):
	global docIds, D, testId, goldVals, testNames
	D=0
	testId=0
	with open(filename) as file:
		for line in file:
			cols=line.rstrip().split("\t")
			year=int(cols[0])

			if year < earliestDate:
				continue

			truth=cols[1]

			doc=cols[2]

			if year == predictionYear:
				if doc not in testData:
					testData[doc]=testId
					testId+=1
			else:
				if doc not in docIds:
					docIds[doc]=D
					D+=1
				winner=1
				if truth == "winner":
					winner=2


				goldVals[docIds[doc]]=winner

		testNames=[""]*len(testData)
		for doc in testData:
			testNames[testData[doc]]=doc

def train():

	global X, Y, logreg

	logreg = linear_model.LogisticRegression(penalty='l2')
	# cross-validated search for best regularization value
	clf = grid_search.GridSearchCV(logreg, {'C':(1e-1, 1e-0, 1e1)})
	logreg=clf.fit(X, Y).best_estimator_
	
def analyzeWeights():
	global featureIds, logreg
	featureNames=[""]*F
	for featureName in featureIds:
		featureNames[featureIds[featureName]]=featureName

	# print the most characteristic features of each class
	zipped=zip(logreg.coef_[0], featureNames)			# zip two lists together to iterate through them simultaneously
	zipped.sort(key = lambda t: t[0], reverse=True)		# sort the two lists by the values in the first (the coefficients)

	print "MOST POSITIVE FEATURES:"
	for (weight, word) in zipped[:10]:
		print "%s\t%.5f" % (word, weight)

	print "\nMOST NEGATIVE FEATURES:"
	for (weight, word) in zipped[:-10:-1]:
		print "%s\t%.5f" % (word, weight)

	print "\nBIAS: %.5f" % logreg.intercept_[0]

def predict():
	global logreg, X_test

	predictions=logreg.predict_proba(X_test)

	posProb=np.zeros(len(predictions))
	for i in range(len(predictions)):

		posProb[i]=predictions[i][1]
	zipped=zip(posProb, testNames)
	zipped.sort(key = lambda t: t[0], reverse=True)		# sort the two lists by the values in the first (their probabilities of winning)

	print "\n###\n# PREDICTIONS\n###\n"
	i=1
	for (prob, doc) in zipped:
		print "%s\t%.3f\t%s" % (i, prob, doc)
		i+=1




featureFile=sys.argv[1]
goldLabels=sys.argv[2]

# start training with data from 1960 on
# predict for year 2015
readGold(goldLabels, 1960, 2015)
readData(featureFile)

train()
analyzeWeights()
predict()


