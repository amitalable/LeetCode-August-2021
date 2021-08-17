# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val, count):
            if root is None:
                return count

            if root.val >= max_val:
                count += 1
                max_val = root.val
            count = dfs(root.left, max_val, count)
            count = dfs(root.right, max_val, count)

            return count
        return dfs(root, -(10**4+1), 0)
