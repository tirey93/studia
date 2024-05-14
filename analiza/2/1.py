import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix

#Wyznacz współczynniki TP, TN, FP, FN i na ich podstawie wyznacz
# dokładność i precyzję (accurancy i precision).

df = pd.read_csv('.\\Data\\kyphosis.csv')


X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test \
    = train_test_split(X, y, random_state=0, test_size=0.30)

dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

dtree_pred = dtree.predict(X_test)
matrix = confusion_matrix(y_test, dtree_pred)
print(matrix)
TN = matrix[0,0]
FP = matrix[0,1]
FN = matrix[1,0]
TP = matrix[1,1]

accuracy = (TN + TP) /(TN + FP + FN + TP)
print(accuracy)
precision = TP / (TP + FP)
print(precision)




