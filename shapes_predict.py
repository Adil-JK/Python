# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:16:21 2021

@author: LENOVO
"""

# With reading a set of data comprising of length, width and diameter of circle,
# this program will predict that the given dimensions are either classified as
# square, rectangle or circle. 
# Note! The data of the csv file needs more features and labels to add in order 
# to increase the accuracy of the prediction. Current prediction accuracy is
# 92.3 %

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("shapes_data.csv")
data.head()

features = data[['Length', 'Width', 'Diameter']]
labels = data[['Label']]

# print(features[['Length','Width']])

# print(labels[['Label']])

clf = KNeighborsClassifier()
clf.fit(features, np.ravel(labels))

pred = clf.predict([[3,3,0]])
print(pred)
pred = clf.predict([[6,1,0]])
print(pred)
pred = clf.predict([[0,0,5]])
print(pred)
pred = clf.predict([[3.5,3.5,0]])
print(pred)

prediction_accuracy = clf.score(features, labels)*100
print("Prediction Accuracy: ", prediction_accuracy)



