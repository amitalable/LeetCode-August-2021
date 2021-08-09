# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp = cur.next
                cur.next = cur.next.next
                temp.next = None
            else:
                cur = cur.next
        return head
