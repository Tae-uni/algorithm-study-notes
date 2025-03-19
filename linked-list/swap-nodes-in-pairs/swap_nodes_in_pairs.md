# Swap Nodes in Pairs (LeetCode #24)
Given a linked list, swap every two adjacent nodes and return its head.  
Must solve the problem without modifying values in the list's nodes.  
(i.e., only nodes themselves may be changed.)

**Constraints:**
> The number of nodes in the list is in the range `[0, 100]`.  
> `0 <= Node.val <= 100`.

ex1:  
Input: head = [1,2,3,4]  
Output: [2,1,4,3]

---

## Solution Approaches
### Approach 1: Iterative
**Code:** [Swap Nodes in Pairs - Iterative](swap_nodes_in_pairs_iterative.py)
```python
def swapPairs(self, head: ListNode) -> ListNode:
    # Create a dummy node
    root = prev = ListNode(None)    # Root: The actual head will be modified, so return `root.next` instead.
    prev.next = head 
    
    while head and head.next:
        b = head.next
        head.next = b.next    # Link first node to the next pair.
        b.next = head    # Swap first and second node.
        
        prev.next = b    # Connect previous swapped pair to current pair.
        
        # Move pointers forward for next swap.
        head = head.next
        prev = prev.next.next
        
    # Skipping dummy node.
    return root.next
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Iterate through the list once.
- Space Complexity: `O(1)` Only a few pointers.

---

### Approach 2: Recursive
**Code:** [Swap Nodes in Pairs - Recursive](swap_nodes_in_pairs_recursive.py)
```python
def swapPairs(self, head: ListNode) -> ListNode:
    # Base Case
    if head and head.next:
        p = head.next
        
        # Recursive call: Swap remaining pairs.
        head.next = self.swapPairs(p.next)
        
        p.next = head
        return p
    
    return head
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Visit each node once.
- Space Complexity: `O(n)` Recursive function call stack.

---

## 🔥 Final Thoughts
Both approaches efficiently solve the `Swap Nodes in Pairs` problem in `O(n)`.  
- Approach 1 (Iterative): More efficient `O(1)`.
- Approach 2 (Recursive): Simper and intuitive but it requires extra space `O(n)`.

**Details about explanation of Recursive, Iterative - [Click](../merge-two-sorted-lists/merge_two_sorted_list.md)*

---

## References
[LeetCode #24](https://leetcode.com/problems/swap-nodes-in-pairs/description/)