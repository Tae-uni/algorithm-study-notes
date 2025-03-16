from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Reverse the linked list.
    def reverseList(self, head: ListNode) -> ListNode:
        curr, prev = head, None

        while curr:
            temp, curr.next = curr.next, prev
            prev, curr = curr, temp

        return prev

    # Convert linked list to python list.
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # Convert python list to linked list.
    def toReverseLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(int(r))
            node.next = prev
            prev = node

        return node


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(resultStr))