import numpy as np

class LogisticRegression:
    def __init__(self, num_steps=1000, learning_rate=0.01):
        self.num_steps = num_steps
        self.learning_rate = learning_rate

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def fit(self, X, y):
        X = X.to_numpy()
        y = y.to_numpy()

        self.weight = np.zeros(X.shape[1])
        self.intercept = 0
        num_samples = X.shape[0]

        for _ in range(self.num_steps):
            prediction = self.sigmoid(X @ self.weight + self.intercept)
            error = prediction - y

            intercept_change = np.sum(error) / num_samples
            slope_change = X.T @ error / num_samples

            self.intercept -= self.learning_rate * intercept_change
            self.weight -= self.learning_rate * slope_change

    def predict(self, X):
        res = self.sigmoid(X @ self.weight + self.intercept)
        return np.where(res >= 0.5, 1, 0)