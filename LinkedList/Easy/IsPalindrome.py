class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow_ptr = fast_ptr = head
        prev = None

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        cur = slow_ptr
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        temp_head = head

        while temp_head and temp_head != slow_ptr and prev:
            if temp_head.val != prev.val:
                return False
            temp_head = temp_head.next
            prev = prev.next
        return True
