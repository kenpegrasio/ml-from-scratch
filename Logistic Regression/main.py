import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from LogisticRegression import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('diabetes.csv')
features = df[['Pregnancies', 'Glucose']]
target = df['Outcome']

model = LogisticRegression()
model.fit(features, target)
predictions = model.predict(features)
accuracy = accuracy_score(target, predictions)
print(accuracy)