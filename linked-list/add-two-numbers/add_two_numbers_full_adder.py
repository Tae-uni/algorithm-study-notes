from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sums = 0
            if l1:
                sums += l1.val
                l1 = l1.next

            if l2:
                sums += l2.val
                l2 = l2.next

            carry, val = divmod(sums + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
