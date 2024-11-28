import unittest
import numpy as np

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.aggregated_score import compute_aggregated_threat_score
from analysis.weighted_average import calculate_weighted_average
from analysis.z_score_adjustment import adjust_for_outliers
from data.data_generator import generate_random_data


def load_test_data(filename):
    """
    Load test data from a text file.

    Parameters:
        filename (str): Name of the file containing the data.

    Returns:
        list of np.array: Loaded data as a list of NumPy arrays.
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # Convert space-separated string back to NumPy array
            department_data = np.array(list(map(float, line.strip().split())))
            data.append(department_data)
    return data

class TestCombinedApproach(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load the test data once for all test cases."""
        cls.departments_data = load_test_data('test_data.txt')

    def test_weighted_average(self):
        departments = [np.mean(self.departments_data[0]), np.mean(self.departments_data[1])]
        result = calculate_weighted_average(departments)
        expected = (departments[0] + departments[1]) / len(departments)
        self.assertAlmostEqual(result, expected)

    def test_weighted_average_equal_weights(self):
        departments = [np.mean(self.departments_data[0])]
        result = calculate_weighted_average(departments)
        expected = np.mean(departments)
        self.assertAlmostEqual(result, expected)

    def test_adjust_for_outliers(self):
        means = [np.mean(dept) for dept in self.departments_data]
        adjusted = adjust_for_outliers(means, threshold=2)
        mean_adjusted = np.mean(adjusted)
        std_dev_adjusted = np.std(adjusted)
        self.assertTrue(all(abs((x - mean_adjusted) / std_dev_adjusted) <= 2 for x in adjusted))

    def test_adjust_for_outliers_all_adjusted(self):
        means = [np.mean(dept) for dept in self.departments_data]
        threshold = 1
        adjusted = adjust_for_outliers(means, threshold=threshold)

        mean = np.mean(means)
        std_dev = np.std(means)
        max_allowed = mean + (threshold * std_dev)
        min_allowed = mean - (threshold * std_dev)
        self.assertTrue(all(min_allowed <= x <= max_allowed for x in adjusted),
                        f"All adjusted values should be within the range [{min_allowed}, {max_allowed}].")

    def test_combined_aggregated_score_zero_mean_data(self):
        zero_mean_data = [np.zeros(len(dept)) for dept in self.departments_data]
        score = compute_aggregated_threat_score(zero_mean_data, z_threshold=2)
        self.assertTrue(0 <= score <= 90, "The score should be within the valid range [0, 90].")

    def test_combined_aggregated_score(self):
        score = compute_aggregated_threat_score(self.departments_data, z_threshold=2)
        self.assertTrue(0 <= score <= 90)

    def test_combined_aggregated_score_high_z_threshold(self):
        score = compute_aggregated_threat_score(self.departments_data, z_threshold=10)
        self.assertTrue(0 <= score < 90)

    def test_combined_aggregated_score_low_z_threshold(self):
        score = compute_aggregated_threat_score(self.departments_data, z_threshold=1)
        self.assertTrue(0 <= score < 90)

    def test_generate_random_data(self):
        # Assuming first department has known properties from the file
        data = self.departments_data[0]
        self.assertTrue(np.all(data >= 0) and np.all(data <= 90), "Data should be within the valid range (0, 90).")

    def test_all_departments_same_threat_scores(self):
        same_score_data = [self.departments_data[5],self.departments_data[6], self.departments_data[7], self.departments_data[8]]
        score = compute_aggregated_threat_score(same_score_data, z_threshold=2)
        dep_means = [np.mean(self.departments_data[5]),np.mean(self.departments_data[6]), np.mean(self.departments_data[7]), np.mean(self.departments_data[8])]
        print(dep_means)
        print(score)
        self.assertTrue(score == np.mean(dep_means))

    def test_one_department_high_score_others_low(self):
        mixed_score_data = [self.departments_data[0],self.departments_data[3], self.departments_data[9],self.departments_data[10], self.departments_data[11], self.departments_data[12]]
        score = compute_aggregated_threat_score(mixed_score_data, z_threshold=3)
        highes_dep_score = np.mean(self.departments_data[9])
        self.assertTrue(highes_dep_score - 10 <= score < highes_dep_score + 10, "Score should reflect the higher score department influence.")

    def test_all_departments_same_mean_threat_score(self):
        same_mean_data = [np.linspace(10, 90, len(dept)) for dept in self.departments_data]
        score = compute_aggregated_threat_score(same_mean_data, z_threshold=2)
        expected_mean = np.mean([np.mean(dept) for dept in same_mean_data])
        self.assertAlmostEqual(score, expected_mean, "Score should match the same mean across all departments.")

    # def test_all_departments_different_number_of_users(self):
    #     # Modify the loaded data to vary department sizes
    #     varied_user_data = [self.departments_data[0],
    #                         np.concatenate([self.departments_data[1], self.departments_data[1]])]
    #     score = compute_aggregated_threat_score(varied_user_data, z_threshold=2)
    #     self.assertTrue(0 <= score <= 90, "Score should handle varying department sizes correctly.")
if __name__ == "__main__":
    unittest.main()
