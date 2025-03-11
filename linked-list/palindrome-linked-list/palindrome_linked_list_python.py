from __future__ import annotations
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Using Deque(Double-ended que), `O(1)` time complexity.
            values: Deque = collections.deque()
        """
        values: List = []

        # Empty array.
        if not head:
            return True

        node = head

        # Convert List
        while node is not None:
            values.append(node.val)
            node = node.next

        # Distinct Palindrome
        while len(values) > 1:
            # Deque, if values.popleft() != values.pop():
            if values.pop(0) != values.pop():
                return False

        return True
