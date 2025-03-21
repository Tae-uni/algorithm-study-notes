from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        odd_ptr, even_ptr = odd_dummy, even_dummy

        curr = head
        idx = 1
        while curr:
            if idx % 2 == 1:
                odd_ptr.next = curr
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = curr
                even_ptr = even_ptr.next
            curr = curr.next
            idx += 1

        even_ptr.next = None
        odd_ptr.next = even_dummy.next

        return odd_dummy.next