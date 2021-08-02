# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums1 = sorted(nums)
        hashmap = {}
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return (hashmap[target-num], i)
            else:
                hashmap[num] = i


print(Solution().twoSum([-1, -2, -3, -4, -5], -8))
