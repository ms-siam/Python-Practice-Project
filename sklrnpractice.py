import numpy as np
#Feature array
X = np.array([[-1,-1],[-2,-1], [-3,-2], [1,1], [2, 1], [3, 2]])
#Label Array
Y = np.array([1,1,1,2,2,2])
from sklearn.naive_bayes import GaussianNB
#Create a classifier
clf = GaussianNB()
#Fitting two arguments in classifier clf
clf.fit(X, Y)

