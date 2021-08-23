# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.seen = []

        def dfs(root):
            if root is None:
                return False
            if root.val in self.seen:
                return True
            self.seen.append(k-root.val)
            if dfs(root.left) or dfs(root.right):
                return True
            return False
        return dfs(root)
