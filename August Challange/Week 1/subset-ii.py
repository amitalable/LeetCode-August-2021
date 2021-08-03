# https://leetcode.com/problems/subsets-ii
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.solve(0, nums, [])
        return self.ans

    def solve(self, idx, nums, ds):
        self.ans.append(ds[:])
        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i-1]:
                continue
            ds.append(nums[i])
            self.solve(i+1, nums, ds)
            ds.pop()
