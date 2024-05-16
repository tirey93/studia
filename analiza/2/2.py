
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix

#2. Załaduj plik "heart.csv" i stwórz dla tych danych model Decision Tree lub Random Forest

df = pd.read_csv('.\\Data\\heart.csv')

X = df.drop('target',axis=1)
y = df['target']

X_train, X_test, y_train, y_test \
    = train_test_split(X, y, random_state=0, test_size=0.30)

dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

dtree_pred = dtree.predict(X_test)
matrix = confusion_matrix(y_test, dtree_pred)
print(matrix)