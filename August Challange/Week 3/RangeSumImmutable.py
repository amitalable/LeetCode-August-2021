# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:
    def __init__(self, nums):
        self.sum_array = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sum_array[i+1] = self.sum_array[i]+nums[i]

    def sumRange(self, left, right):
        return self.sum_array[right+1]-self.sum_array[left]
