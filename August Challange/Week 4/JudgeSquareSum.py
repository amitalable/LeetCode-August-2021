# https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = list(map(lambda x: x*x, range(int(c**0.5+1))))
        start = 0
        end = len(l)-1
        while end >= start:
            temp = l[end] + l[start]
            if temp > c:
                end -= 1
            elif temp < c:
                start += 1
            else:
                return True
        return False


print(Solution().judgeSquareSum(5))
