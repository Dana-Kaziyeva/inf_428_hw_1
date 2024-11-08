import unittest
import pandas as pd

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.feature_extraction import extract_time_features


class TestFeatureExtraction(unittest.TestCase):

    def test_extract_time_features(self):
        # Create a sample DataFrame
        df = pd.DataFrame({'timestamp': pd.to_datetime(['2024-11-08 09:00:00'])})
        df = extract_time_features(df)

        # Check if the new columns are added
        self.assertIn('hour', df.columns)
        self.assertIn('minute', df.columns)
        self.assertIn('day_of_week', df.columns)

        # Check the extracted values
        self.assertEqual(df['hour'].iloc[0], 9)
        self.assertEqual(df['minute'].iloc[0], 0)
        self.assertEqual(df['day_of_week'].iloc[0], 4)  # Friday (0=Monday, 6=Sunday)

    def test_extract_multiple_timestamps(self):
        # Test with multiple timestamps
        df = pd.DataFrame({
            'timestamp': pd.to_datetime(['2024-11-08 09:00:00', '2024-11-09 18:30:00'])
        })
        df = extract_time_features(df)

        # Check the extracted values
        self.assertEqual(df['hour'].iloc[1], 18)
        self.assertEqual(df['minute'].iloc[1], 30)
        self.assertEqual(df['day_of_week'].iloc[1], 5)  # Saturday

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame({'timestamp': pd.to_datetime([])})
        df = extract_time_features(df)

        # Ensure no rows exist but columns are added
        self.assertTrue(df.empty)
        self.assertListEqual(list(df.columns), ['timestamp', 'hour', 'minute', 'day_of_week'])


if __name__ == '__main__':
    unittest.main()
