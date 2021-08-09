# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        mydict = dict()
        temp1 = headA
        temp2 = headB
        while(temp1):
            mydict[temp1] = temp1.val
            temp1 = temp1.next
        while(temp2):
            if temp2 in mydict:
                return temp2
            temp2 = temp2.next
