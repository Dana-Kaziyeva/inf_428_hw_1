from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # result = []
        # for i in nums1:
        #     if i in nums2 and i not in result:
        #         result.append(i)
        #
        # return result

        return list(set(nums1) & set(nums2))

