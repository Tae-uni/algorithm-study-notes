# Odd Even Linked List (LeetCode #328)
Given the `head` of a singly linked list.  
The first node is considered **odd**, and the second node is **even**.  
Solve the problem in `O(1)` space complexity and `O(n)` time complexity.

**Constraints:**
> The number of nodes in the linked list is in the range `[0, 10^4]`.  
> `-10^6 <= Node.val <= 10^6`

ex1:  
Input: head = [1,2,3,4,5]  
Output: [1,3,5,2,4]

ex2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

---

## Solution Approaches
### Approach 1: In-place Separation
Separate odd and even indexed nodes by rearranging pointers.  
Directly in the original list.  
To understand the concept of the logic, think of separate nodes `odd_head` and `even_head` using two pointers.  
Add the value to each head and keep loop. At the end, connect two head to one linked list.  

**But remember, this is only use pointers not extra list so it is in-place way.**

**Code:** [Odd Even Linked List - In_place](odd_even_linked_list_in_place.py)
```python
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next
    
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
        
    odd.next = even_head
    return head
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Traverses the list once to rearrange.
- Space Complexity: `O(1)` Only uses a few pointers.

---

### Approach 2: Split with Dummy Nodes

Creates two separate linked lists (one for odd-indexed, one for even-indexed) using dummy head nodes.  
After processing, the two lists are merged.

**Code:** [Odd Even Linked List - Dummy](odd_even_linked_list_dummy.py)
```python
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    
    odd_dummy = ListNode(0)
    even_dummy = ListNode(0)
    odd_ptr, even_ptr = odd_dummy, even_dummy
    
    curr = head
    idx = 1
    while curr:
        if curr % 2 == 1:    # If the position is odd.
            odd_ptr.next = curr
            odd_ptr = odd_ptr.next
        else:
            even_ptr.next = curr
            even_ptr = even_ptr.next
            
        curr = curr.next
        idx += 1
        
    # Terminate the even list.
    even_ptr.next = None
    odd_ptr.next = even_dummy.next
    
    return odd_dummy.next
```


#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Iterates through the list once.
- Space Complexity: `O(1)` Uses dummy nodes and pointers.

---

## 🔥 Final Thoughts
Both approaches efficiently solve the `Odd Even Linked List` problem in `O(n)` time and `O(1)` space.  
They share the same core logic: separating nodes by index (odd/even) and reconnecting them at the end.  
I think the Approach 1 (In-place Separation) better way to solve due to not use extra dummy lists.

---

## References
[LeetCode #328](https://leetcode.com/problems/odd-even-linked-list/)