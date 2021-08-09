# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = cur = ListNode(0, head)
        while head:
            if head.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            head = head.next
        return ptr.next
