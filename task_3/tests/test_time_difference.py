import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.time_difference import time_difference_in_hours


class TestTimeDifference(unittest.TestCase):

    def test_time_difference(self):
        # Basic test case: difference between 23:00 and 01:00
        self.assertEqual(time_difference_in_hours(23, 1), 2)

    def test_time_difference_edge_case(self):
        # Edge case: difference between the same time
        self.assertEqual(time_difference_in_hours(12, 12), 0)

    def test_wraparound_case(self):
        # Wraparound midnight: difference between 2:00 and 23:00
        self.assertEqual(time_difference_in_hours(2, 23), 3)

    def test_reverse_difference(self):
        # Reverse case: difference between 1:00 and 23:00
        self.assertEqual(time_difference_in_hours(1, 23), 2)

    def test_no_difference(self):
        # No difference: difference between 0:00 and 0:00
        self.assertEqual(time_difference_in_hours(0, 0), 0)

    def test_half_day_difference(self):
        # Half day difference: difference between 6:00 and 18:00
        self.assertEqual(time_difference_in_hours(6, 18), 12)

    def test_max_difference(self):
        # Max difference that should still wrap around
        self.assertEqual(time_difference_in_hours(0, 23), 1)
        self.assertEqual(time_difference_in_hours(23, 0), 1)


if __name__ == '__main__':
    unittest.main()
