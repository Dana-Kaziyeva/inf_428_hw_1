import unittest
import numpy as np
from sklearn.linear_model import LinearRegression

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.model_evaluation import evaluate_model


class TestModelEvaluation(unittest.TestCase):

    def setUp(self):
        """
        Prepare sample data for testing.
        """
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])
        self.model = LinearRegression().fit(X, y)
        self.X_test = np.array([[6], [7]])
        self.y_test = np.array([12, 14])

    def test_model_evaluation(self):
        """
        Test the model evaluation function.
        """
        mse = evaluate_model(self.model, self.X_test, self.y_test)
        self.assertLess(mse, 1)


if __name__ == '__main__':
    unittest.main()
