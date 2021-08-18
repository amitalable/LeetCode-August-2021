# https://leetcode.com/problems/decode-ways
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)

        dp[0], dp[1] = 1, 1
        if s[0] == '0':
            return 0

        for i in range(2, n+1):
            val = int(s[i-1])
            two_dig = int(s[i-2]+s[i-1])

            if val != 0:
                dp[i] = dp[i-1]
            if 10 <= two_dig <= 26:
                dp[i] += dp[i-2]

        return dp[-1]


obj = Solution()
print(obj.numDecodings('226'))
