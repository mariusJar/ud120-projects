#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#clf = SVC(kernel='linear')
#C (say, 10.0=0.616, 100.=0.616, 1000.=0.8214, and 10000.=0.892). Which value of C gives the best accuracy?
clf = SVC(C=10000, kernel='rbf')

## reducing training data set by 99%
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)

chris_total = 0
for i in pred:
    chris_total = chris_total + i
    
print("Test total:", len(pred))
print("Chris total:", chris_total)
# print("prediction 10th email:", pred[10])
# print("prediction 26th email:", pred[26])
# print("prediction 50th email:", pred[50])
print("prediction time:", round(time()-t1, 3), "s")
accuracy = accuracy_score(pred, labels_test)
print("accuracy: ", accuracy)

#########################################################


