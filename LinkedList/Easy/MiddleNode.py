# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = prev = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next

        return prev
