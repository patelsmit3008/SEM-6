# Simple Linear Regression without Libraries

class SimpleLinearRegression:
    def __init__(self):
        self.m = 0  # Slope
        self.b = 0  # Intercept

    def fit(self, X, y):
        """Train the model using Least Squares Method"""
        n = len(X)
        sum_x = sum(X)
        sum_y = sum(y)
        sum_xy = sum(X[i] * y[i] for i in range(n))
        sum_x2 = sum(X[i] ** 2 for i in range(n))

        # Calculating slope (m) and intercept (b)
        self.m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        self.b = (sum_y - self.m * sum_x) / n

    def predict(self, X):
        """Make predictions"""
        return [self.m * x + self.b for x in X]

# Example Usage
X = [1, 2, 3, 4, 5]  # Feature values
y = [2, 3, 5, 4, 6]  # Target values

model = SimpleLinearRegression()
model.fit(X, y)  # Train the model
predictions = model.predict([5, 5])  # Predict for new values

print("Predictions:", predictions)