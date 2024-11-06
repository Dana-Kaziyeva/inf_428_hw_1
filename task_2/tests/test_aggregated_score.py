import unittest

import numpy as np
from analysis.aggregated_score import compute_aggregated_threat_score
from analysis.weighted_average import calculate_weighted_average
from analysis.z_score_adjustment import adjust_for_outliers
from data.data_generator import generate_random_data


class TestCombinedApproach(unittest.TestCase):

    def test_weighted_average(self):
        departments = [np.array([10, 20, 30]), np.array([40, 50, 60])]
        weights = [2, 3]
        result = calculate_weighted_average(departments, weights)
        expected = (20 * 2 + 50 * 3) / 5
        self.assertAlmostEqual(result, expected)

    def test_adjust_for_outliers(self):
        means = [10, 50, 90, 15, 85]
        adjusted = adjust_for_outliers(means, threshold=2)
        mean_adjusted = np.mean(adjusted)
        std_dev_adjusted = np.std(adjusted)
        self.assertTrue(all(abs((x - mean_adjusted) / std_dev_adjusted) <= 2 for x in adjusted))

    def test_combined_aggregated_score(self):
        departments = [generate_random_data(30, 5, 100), generate_random_data(70, 10, 150)]
        weights = [1, 2]
        score = compute_aggregated_threat_score(departments, weights, z_threshold=2)
        self.assertTrue(0 <= score < 90)


if __name__ == "__main__":
    unittest.main()
