import numpy as np

class LinearRegression:
    def __init__(self, num_steps=1000, learning_rate=0.01):
        self.num_steps = num_steps
        self.learning_rate = learning_rate

    def fit(self, X, y):
        X = X.to_numpy()
        y = y.to_numpy()

        self.X_mean = np.mean(X, axis=0)
        self.X_std = np.std(X, axis=0)
        self.y_mean = np.mean(y)
        self.y_std = np.std(y)

        X = (X - self.X_mean) / self.X_std
        y = (y - self.y_mean) / self.y_std

        self.weight = np.zeros(X.shape[1])
        self.intercept = 0
        num_samples = X.shape[0]

        for _ in range(self.num_steps):
            predictions = X @ self.weight + self.intercept
            error = y - predictions

            intercept_change = -2 * np.sum(error) / num_samples
            slope_change = -2 * (X.T @ error) / num_samples

            self.intercept -= self.learning_rate * intercept_change
            self.weight -= self.learning_rate * slope_change

    def predict(self, X):
        X = X.to_numpy().reshape(-1, 1)
        X = (X - self.X_mean) / self.X_std
        return (X @ self.weight + self.intercept) * self.y_std + self.y_mean 