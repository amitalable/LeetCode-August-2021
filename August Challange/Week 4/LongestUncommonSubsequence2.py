# https://leetcode.com/problems/longest-uncommon-subsequence-ii/
class Solution:
    def findLUSlength(self, A: List[str]) -> int:
        
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
        
        A.sort(key = len, reverse=True)
        for i, s in enumerate(A):
            found = False
            for j, ss in enumerate(A):
                if i == j:
                    continue
                if isSubsequence(s, ss):
                    found = True
                    break
            if not found:
                return len(s)
        return -1