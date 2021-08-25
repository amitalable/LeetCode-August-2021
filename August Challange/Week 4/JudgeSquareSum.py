# https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(c**0.5)
        while end >= start:
            temp = start**2 + end**2
            if temp > c:
                end -= 1
            elif temp < c:
                start += 1
            else:
                return True
        return False


print(Solution().judgeSquareSum(5))
