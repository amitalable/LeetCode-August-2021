# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1
        for node in nodes:
            if slots <= 0:
                return False
            slots += -1 if node == '#' else 1
        return slots == 0


obj = Solution()
print(obj.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
