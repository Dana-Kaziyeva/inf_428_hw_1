import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.time_difference import time_difference_in_hours


class TestTimeDifference(unittest.TestCase):

    def test_time_difference(self):
        # Test for the time difference calculation
        self.assertEqual(time_difference_in_hours(23, 1), 2)  # 23:00 and 01:00 is 2 hours

    def test_time_difference_edge_case(self):
        # Test for edge cases like same time
        self.assertEqual(time_difference_in_hours(12, 12), 0)  # 12:00 and 12:00 should be 0 hours


if __name__ == '__main__':
    unittest.main()
