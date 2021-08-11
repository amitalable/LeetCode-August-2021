from typing import Counter, List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for key in sorted(count, key=abs):
            if count[key] > count[2*key]:
                return False
            count[2*key] -= count[key]
        return True


arr = [3, 1, 3, 6]
print(Solution().canReorderDoubled(arr))
