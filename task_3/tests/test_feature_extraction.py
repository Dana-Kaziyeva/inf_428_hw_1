import unittest
import pandas as pd

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.feature_extraction import extract_time_features


class TestFeatureExtraction(unittest.TestCase):

    def test_extract_time_features(self):
        """
        Test feature extraction from a timestamp column.
        """
        # Create a sample DataFrame
        df = pd.DataFrame({'timestamp': pd.to_datetime(['2024-11-08 09:00:00'])})

        # Extract features
        df = extract_time_features(df)

        # Test if the new columns are added
        self.assertIn('hour', df.columns)
        self.assertIn('minute', df.columns)
        self.assertIn('day_of_week', df.columns)


if __name__ == '__main__':
    unittest.main()
