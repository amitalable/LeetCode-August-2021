# https://leetcode.com/problems/range-addition-ii
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n
        for x, y in ops:
            min_m = min(min_m, x)
            min_n = min(min_n, y)
        return min_m * min_n
