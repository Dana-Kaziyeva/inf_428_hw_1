from typing import List

class Solution(object):
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = 1
        longest = 1
        for i in range(0, len(nums) - 1):  
            if nums[i] < nums[i + 1]:
                n += 1
            else:
                longest = max(n, longest)
                n = 1

        return max(n, longest)
