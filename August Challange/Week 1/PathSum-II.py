# https://leetcode.com/problems/path-sum-ii/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.l = []

        def dfs(root, targetList):
            if root is None:
                return targetList
            targetList.append(root.val)
            if sum(targetList) == targetSum:
                self.l.append(targetList[:])
            targetList = dfs(root.left, targetList)
            targetList = dfs(root.right, targetList)
            targetList.pop()
            return targetList
        dfs(root, [])
        return self.l


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

obj = Solution()
print(obj.pathSum(root, 22))
