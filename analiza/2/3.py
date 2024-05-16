#Dla danych Kyphosis określ dokładność w zależności od ilości drzew
# w algorytmie Random Forest (narysuj wykres)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

df = pd.read_csv('.\\Data\\kyphosis.csv')


X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test \
    = train_test_split(X, y, random_state=0, test_size=0.30)

def get_accuracy(X_train, y_train, n_estimators):
    rfc = RandomForestClassifier(n_estimators=n_estimators)
    rfc.fit(X_train, y_train);

    rfc_pred = rfc.predict(X_test)

    matrix = confusion_matrix(y_test, rfc_pred)
    print(matrix)
    TN = matrix[0, 0]
    FP = matrix[0, 1]
    FN = matrix[1, 0]
    TP = matrix[1, 1]

    return (TN + TP) / (TN + FP + FN + TP)