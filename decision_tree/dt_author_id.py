#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train,labels_train)

# result = clf.predict(features_test)
# count = 0
# for i,j in zip(result, labels_test):
#     if ( i == j):
#         count += 1;
#
# print count/len(result) * 100
print "Accuracy: {}", clf.score(features_test,labels_test)

#########################################################
### your code goes here ###


#########################################################


