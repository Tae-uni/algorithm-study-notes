# Add Two Numbers (LeetCode #2)
Given two `non-empty` linked lists representing two non-negative integers.  
The digits are stored in reverse order.  
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Constraints:**
> The number of nodes in each linked list is in the range `[1, 100]`.  
> `0 <= Node.val <= 9`  
> It is guaranteed that the list represents a number that does not have leading zeros.

ex1:  
Input: l1 = [2,4,3], l2 = [5,6,4]  
Output: [7,0,8]   
Explanation: 342 + 465 = 807.

---

## Solution Approaches
### Approach 1: Full Adder (Recommended)
**Code:** [Add Two Numbers - Full Adder](add_two_numbers_full_adder.py)
```python
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node to store the result.
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
        # Create a new node and attach it to the result list.
        head.next = ListNode(val)
        head = head.next

    return root.next
```
---

#### What is `divmod`?
Returns both the quotient and remainder when dividing `a` by `b`. 
```python
quotient, remainder = divmod(a, b)
```
- quotient = a // b → The integer result of division.
- remainder = a % b → The remainder after division.

---

#### ⏳ Time & Space Complexity
- Time Complexity: `O(max(n,m))` Iterates through both lists once.
- Space Complexity: `O(max(n,m))` Stores the new linked list in the worst case.

---

### Approach 2: Reverse & Convert (Inefficient)
**Code:** [Add Two Numbers - Reverse Convert](add_two_numbers_reverse_convert.py)
```python
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

```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n+m) + O(k) + O(k)` = `O(max(n,m))` Reversal + Conversion + Reconstruction
- Space Complexity: `O(n+m+k)` = `O(max(n,m))` Stores full lists in memory

---

## 🔥 Final Thoughts
Approach1 (Full Adder) is the best way to solve `Add Two Numbers` problem efficiently.  
However, the Approach2 (Reverse & Convert) is valid but inefficient way to solve the problem due to unnecessary conversions.

Alternative Approach to Study:
- Stack-Based Approach
- Recursive Approach

---

## References
[LeetCode #2](https://leetcode.com/problems/add-two-numbers/description/)