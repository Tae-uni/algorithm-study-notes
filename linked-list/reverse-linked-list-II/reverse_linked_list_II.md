# Reverse Linked List II (LeetCode #92)

Given the `head` of singly linked lists.  
Two integers `lift` and `right` where `left <= right`  
Reverse the nodes of the list from position left to right, and return the **reversed** list.

**Constraints:**
> The number of nodes in the list in `n`.  
> `1 <= n <= 500`  
> `-500 <= Node.val <= 500`  
> `1 <= left <= right <= n`

ex1:  
Input: head = [1,2,3,4,5], left = 2, right = 4  
Output: [1,4,3,2,5]

---

## Solution Approaches
### Approach 1: Iterative -dummy (Recommended)
**Code:** [Reverse Linked List - Dummy](reverse_linked_list_iterative_dummy.py)
```python
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    # Create dummy.val = 0, dummy.next = head.
    # When there's possibility to change the Original value such as Insert, Delete, Reverse.
    dummy = ListNode(0, head)
    prev = dummy
    
    # This is linked list, so cannot approach prev right away.
    for _ in range(left - 1):
        prev = prev.next

    # Right before reverse the list. fixed.
    curr = prev.next

    # Reverse the list.   
    for _ in range(right - left):
        next_node = curr.next 
        # curr.next, next_node.next, prev.next = next_node.next, prev.next, next_node
        curr.next = next_node.next
        next_node.next = prev.next    # Insert next_node right after prev
        prev.next = next_node    # Link prev to next_node

    return dummy.next
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Traverse the list once to reach the reversal and up to `right - left` times to reverse.
- Space Complexity: `O(1)` In-place reversal using constant pointers.

---

### Approach 2: Iterative
**Code:** [Reverse Linked List - Iterative](reverse_linked_list_iterative.py)
```python
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    # Creating dummy nodes.
    root = start = ListNode(0)
    root.next = head

    for _ in range(left - 1):
        start = start.next

    end = start.next

    for _ in range(right - left):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp

    return root.next
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Traverse the list once to reach the reversal and up to `right - left` times to reverse.
- Space Complexity: `O(1)` In-place reversal using constant pointers.

---

## 🔥 Final Thoughts
Both approaches use a dummy node and perform in-place reversal with two pointers in `O(n)` time and `O(1)` space.  
The key difference lies in pointer naming and how the reversal is expressed.  

- Approach 1: uses `prev`,`curr`, and `next_node`. Clear name of the pointer, Manipulate step by step.  
- Approach 2: uses `start`, `end`, and `tmp`. Similar logic but slightly different variable tracking style.

Approach 1 is easier to understand and more explict.

---

## References
[LeetCode #92](https://leetcode.com/problems/reverse-linked-list-ii/description/)