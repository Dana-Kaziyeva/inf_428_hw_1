import unittest
import numpy as np

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.aggregated_score import compute_aggregated_threat_score
from analysis.weighted_average import calculate_weighted_average
from analysis.z_score_adjustment import adjust_for_outliers
from data.data_generator import generate_random_data


class TestCombinedApproach(unittest.TestCase):

    def test_weighted_average(self):
        departments = [np.mean([10, 20, 30]), np.mean([40, 50, 60])]
        weights = [2, 3]
        result = calculate_weighted_average(departments, weights)
        expected = (20 * 2 + 50 * 3) / 5
        self.assertAlmostEqual(result, expected)

    def test_weighted_average_zero(self):
        departments = [10, 20, 30]
        weights = [0, 0, 0]
        result = calculate_weighted_average(departments, weights)
        self.assertEqual(result, 0)

    def test_weighted_average_equal_weights(self):
        departments = [10, 20, 30]
        weights = [1, 1, 1]
        result = calculate_weighted_average(departments, weights)
        expected = np.mean(departments)
        self.assertAlmostEqual(result, expected)

    def test_weighted_average_large_numbers(self):
        departments = [1000, 2000, 3000]
        weights = [5, 10, 15]
        result = calculate_weighted_average(departments, weights)
        expected = (1000 * 5 + 2000 * 10 + 3000 * 15) / 30
        self.assertAlmostEqual(result, expected)

    def test_adjust_for_outliers(self):
        means = [10, 50, 90, 15, 85]
        adjusted = adjust_for_outliers(means, threshold=2)
        mean_adjusted = np.mean(adjusted)
        std_dev_adjusted = np.std(adjusted)
        self.assertTrue(all(abs((x - mean_adjusted) / std_dev_adjusted) <= 2 for x in adjusted))

    def test_adjust_for_outliers_all_adjusted(self):
        means = [1, 2, 3, 1000, 5]
        adjusted = adjust_for_outliers(means, threshold=1)
        self.assertTrue(all(x == 5 for x in adjusted))

    def test_adjust_for_outliers_single_value(self):
        means = [100]
        adjusted = adjust_for_outliers(means, threshold=3)
        self.assertEqual(adjusted, means)

    def test_combined_aggregated_score(self):
        departments = [generate_random_data(30, 5, 100), generate_random_data(70, 10, 150)]
        weights = [1, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(0 <= score < 90)

    def test_combined_aggregated_score_large_data(self):
        departments = [generate_random_data(100, 10, 1000), generate_random_data(150, 15, 1000)]
        weights = [3, 5]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(0 <= score < 100)

    def test_combined_aggregated_score_zero_weights(self):
        departments = [generate_random_data(30, 5, 100), generate_random_data(70, 10, 150)]
        weights = [0, 0]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertEqual(score, 0)

    def test_combined_aggregated_score_equal_weights(self):
        departments = [generate_random_data(50, 5, 100), generate_random_data(60, 5, 100)]
        weights = [1, 1]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(0 <= score < 90)

    def test_combined_aggregated_score_large_outliers(self):
        departments = [generate_random_data(100, 50, 100), generate_random_data(200, 50, 100)]
        weights = [2, 4]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=3)
        self.assertTrue(0 <= score < 200)

    def test_combined_aggregated_score_with_negative_values(self):
        departments = [generate_random_data(-50, 10, 100), generate_random_data(-30, 5, 150)]
        weights = [2, 3]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(-100 <= score < 0)

    def test_combined_aggregated_score_zero_mean_data(self):
        departments = [generate_random_data(0, 10, 100), generate_random_data(0, 5, 150)]
        weights = [1, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(-10 <= score < 10)

    def test_combined_aggregated_score_with_outliers_adjusted(self):
        departments = [generate_random_data(100, 10, 100), generate_random_data(90, 10, 150)]
        weights = [1, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(80 <= score < 100)

    def test_combined_aggregated_score_high_variance(self):
        departments = [generate_random_data(100, 30, 100), generate_random_data(200, 40, 150)]
        weights = [2, 5]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(100 <= score < 300)

    def test_combined_aggregated_score_low_variance(self):
        departments = [generate_random_data(50, 5, 100), generate_random_data(60, 5, 150)]
        weights = [3, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(50 <= score < 70)

    def test_combined_aggregated_score_high_z_threshold(self):
        departments = [generate_random_data(30, 5, 100), generate_random_data(70, 10, 150)]
        weights = [1, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=10)
        self.assertTrue(0 <= score < 90)

    def test_combined_aggregated_score_low_z_threshold(self):
        departments = [generate_random_data(30, 5, 100), generate_random_data(70, 10, 150)]
        weights = [1, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=1)
        self.assertTrue(0 <= score < 90)

    def test_generate_random_data(self):
        data = generate_random_data(50, 10, 100)
        self.assertEqual(len(data), 100)
        self.assertTrue(np.all(data >= 40) and np.all(data <= 60))

    def test_generate_random_data_zero_variance(self):
        data = generate_random_data(50, 0, 100)
        self.assertEqual(len(data), 100)
        self.assertTrue(np.all(data == 50))

    def test_generate_random_data_negative_mean(self):
        data = generate_random_data(-50, 5, 100)
        self.assertEqual(len(data), 100)
        self.assertTrue(np.all(data >= -55) and np.all(data <= -45))

    def test_generate_random_data_large_range(self):
        data = generate_random_data(0, 100, 100)
        self.assertEqual(len(data), 100)
        self.assertTrue(np.all(data >= 0) and np.all(data <= 100))

    def test_generate_random_data_single_sample(self):
        data = generate_random_data(50, 5, 1)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], 50)

if __name__ == "__main__":
    unittest.main()
