# https://leetcode.com/problems/linked-list-cycle
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = nex = head
        while cur and nex and nex.next:
            nex = nex.next.next
            if cur == nex:
                return True
            cur = cur.next
        return False
