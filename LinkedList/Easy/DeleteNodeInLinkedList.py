# https://leetcode.com/problems/delete-node-in-a-linked-list/
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):

        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None
