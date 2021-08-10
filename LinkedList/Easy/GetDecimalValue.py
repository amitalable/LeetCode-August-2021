# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        x = ""
        while head:
            x = x + str(head.val)
            head = head.next
        return int(x, 2)
