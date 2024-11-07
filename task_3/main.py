import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from analysis.time_difference import time_difference_in_hours
from analysis.model_evaluation import evaluate_model
from data.sample_data import generate_sample_data
from sklearn.linear_model import LinearRegression


def main():
    """
    Main entry point to demonstrate various functionalities.
    """
    # Example of using time difference function
    print("Time difference between 23:00 and 01:00:", time_difference_in_hours(23, 1))  # Expected output: 2

    # Example of generating sample data
    data = generate_sample_data()
    print("Sample Data:\n", data)

    # Example of evaluating a model
    model = LinearRegression()
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([1, 2, 3, 4, 5])
    model.fit(X_train, y_train)

    # Evaluating the model with test data
    X_test = np.array([[6], [7]])
    y_test = np.array([6, 7])
    mse = evaluate_model(model, X_test, y_test)
    print("Model evaluation (MSE):", mse)


if __name__ == "__main__":
    main()
