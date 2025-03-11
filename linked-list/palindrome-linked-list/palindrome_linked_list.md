# Palindrome Linked List (LeetCode #234)
Given the `head` of a singly linked list.  
If it is a palindrome return **true** else **false**.

**Constraints:**
> The number of nodes in the list is in the range `[1, 10^5]`.  
> 0 <= Node.val <= 9

ex1:  
Input: head = [1,2,2,1]  
Output: true

---

## The Runner Technique
To solve this problem, we can reverse the first half while finding the middle of the linked list.  
- Fast & Slow Pointers: `fast` moves **two steps** while `slow` moves `one step`.  
- Reversing the First Half: As `slow` moves, reverse the first half of the list (`rev`).  
- Odd-Length Lists: If the list length is odd, skip the middle element.  
- Compare Halves: Finally, compare the reversed first half with the second half.  

**Check the details below.**

---

## Solution Approaches
### Approach 1:  Convert to List
**Code:** [Palindrome Linked List - List](palindrome_linked_list_python.py)
```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    values: List = []
    
    if not head:
        return False

    node = head

    while node is not None:
        values.append(node.val)
        node = node.next

    while len(values) > 1:
        if values.pop(0) != values.pop():
            return False

    return True
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Traverse the list once to copy and another time to check.
- Space Complexity: `O(n)` Stores all values in a list.

---

### Approach 2: Convert to Deque
**Code:** [Palindrome Linked List - Deque](palindrome_linked_list_python.py)
```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
     values: Deque = collections.deque()
     
     if not head:
         return True
     
     node = head
     
     while node is not None:
         values.append(node.val)
         node = node.next
         
     while len(values) > 1:
         if values.pop(0) != values.pop():
             return False
         
     return True
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Similar to Approach 1, tho `deque.popleft()` more efficient.
- Space Complexity: `O(n)` Stores all values in a deque.

---

### Approach 3: Runner (Recommended)
**Code:** [Palindrome Linked List - Runner](palindrome_linked_list_runner.py)  
```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    rev = None
    # `slow` moves one step, `fast` moves two steps.
    slow = fast = head
    
    while fast and fast.next:
        # `fast` moves two steps.
        fast = fast.next.next
        # Reverse the first half while moving `slow` forward.
        rev, rev.next, slow = slow, rev, slow.next

    # If the length is odd, move `slow` one step further.
    if fast:
        slow = slow.next
        
    # Compare are reversed first half with the second half.
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    # If `rev` is completely traversed, it is a palindrome.
    return not rev
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Traverse the list twice(reverse half, compare)
- Space Complexity: `O(1)` Uses only few pointers(rev, slow, fast)

---

## 🔥 Final Thoughts

All approaches efficiently solve the `Palindrome Linked List` problem in `O(n)`.  
Approach 1 & 2 (List & Deque): Straightforward and easy. But it requires extra space `O(n)`.  
Approach 3 (Runner): The most optimized with `O(1)` space. Using two pointers to reverse half of the list.

---

## References
[LeetCode #234](https://leetcode.com/problems/palindrome-linked-list/description/)