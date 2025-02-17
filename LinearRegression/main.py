import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

df = pd.read_csv('data.csv')
features = df[['sqft_living']]
target = df['price']

model = LinearRegression()
model.fit(features, target)
predictions = model.predict(features)


plt.figure(figsize=(8, 6))

plt.scatter(features, target, color='blue', alpha=0.5, label='Actual Prices')
plt.plot(features, predictions, color='red', linewidth=2, label='Predicted Prices')

plt.xlabel('Square Feet Living Area')
plt.ylabel('House Price')
plt.title('Linear Regression')
plt.legend()

plt.show()
