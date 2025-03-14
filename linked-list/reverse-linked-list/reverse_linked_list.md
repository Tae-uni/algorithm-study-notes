# Reverse Linked List (LeetCode #206)
Given `head` of a singly linked list.  
Reverse the list and return it.

**Constraints:**
> The number of nodes range in [0, 5000]  
> -5000 <= Node.val <=5000

ex1:  
Input: head = [1,2,3,4,5]  
Output: [5,4,3,2,1]

**Follow up**: A linked list can be reversed either iteratively or recursively.

---

## Solution Approaches
### Approach 1: Iterative (Recommended)
**Code:** [Reverse Linked List - Iterative](reverse_linked_list_iterative.py)
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr, prev = head, None

    while curr:
        # Before disconnect pointer between `curr` and `curr.next`, put the `curr.next` to the `temp`.
        temp = curr.next
        # Pointer is change `curr` to `prev`
        curr.next = prev

        # Move forward to next node.
        prev = curr
        curr = temp
        
    return prev
```
```
*Head*
None  ->  1  ->  2  ->  3  ->  4  ->  None
  
prev    curr  curr.next
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Traverse the linked list once.
- Space Complexity: `O(1)` Use only a few extra pointers.

---

### Approach 2: Recursive
**Code:** [Reverse Linked List - recursive](reverse_linked_list_recursive.py)
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Base Case: If the list is empty or reaches last node, return head.
    if not head or not head.next:
        return head

    # Recursive Case.
    new_head = self.reverseList(head.next)

    # Reverse the pointer
    head.next.next = head # 2 -> 3 is changed to 3 -> 2.
    head.next = None # Cut the old forward link.

    return new_head
```

**head.next.next = head explanation:**

> linkedlist of 1 => 2 => 3  
base case focuses on 2 => 3 where 2 is the head  
head.next.next = head means 3.next = 2 (the head) so this makes a 2 => 3 circular linked list (which means 2 => 3 & 2 <= 3 exists). 2 is still the head.  
then we must detach 2 => 3(remember we still have 2 <= 3) so head.next = null means we detach 2 => 3.  
Now the result is 2 <= 3.  
Now we go to the next part which is 1 => 2 and repeat.

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Recursively traverse the linked list.
- Space Complexity: `O(n)` Storing the stack through the `n` function calls.

---

## 🔥 Final Thoughts
Both approaches efficiently reverse a linked list in `O(n)`.  
Approach 1(Iterative): More memory-efficient `O(1)` and straightforward.  
Approach 2(Recursive): Simper and more intuitive, but uses extra memory `O(n)`.  

The iterative way is generally preferred and straightforward.

---

## References
- [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/solutions/6072712/video-solution-with-visualization/)
- [Reverse Linked List](https://www.youtube.com/watch?v=G0_I-ZF0S38)