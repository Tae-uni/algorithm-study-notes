# Merge Two Sorted List (LeetCode #21)

The heads of two sorted linked lists `list1`, `list2`.  
Merge the two lists into one **sorted** list.  
Return the head of the merged linked list.

**Constraints:**
> The number of nodes in both lists in the range [0, 50]  
> -100 <= Node.val <= 100  
> Both list1 and list2 are sorted in **non-decreasing** order.

ex1:  
Input: list1 = [1,2,4], list2 = [1,3,4]  
Output: [1,1,2,3,4,4]

```
           node  pointer
    list1 = (1)    ->     (2)     ->     (4)
    list2 = (1)    ->     (3)     ->     (4)
```

---

## Solution Approaches
### Approach 1: Iterative (Recommended)
**Code:** [Merge Two Sorted List - Iterative](merge_sorted_list_iterative.py)
```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy Node.
    dummy = ListNode()
    # Pointer to track the merge list.
    current = dummy 

    # Compare values from `list1` and `list2` and put the smaller one to `current`.
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # After loop, if there are remaining nodes, append them to the end of the merged list.
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n + m)` Iterate through both lists once.
- Space Complexity: `O(1)` Uses only a few pointers.

---

### Approach 2: Recursion
**Code:** [Merge Two Sorted List - Recursion](merge_sorted_list_recursive.py)
```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # If list1 is empty, switch with list2 or list2 is not empty and list1 value is greater than list2 value...
    if (not list1) or (list2 and list1.val > list2.val):
        # Ensure `list1` is always has smaller values.
        list1, list2 = list2, list1
    # Keep recursion until list1 is None. Base case
    if list1:
        list1.next = self.mergeTwoLists(list1.next, list2)
    return list1
```
```
merge([1,2,4], [1,3,4])    # 1 == 1 -> Swap X
    merge([2,4], [1,3,4])    # 2 > 1 -> Swap O (list1 <-> list2)
        merge([3,4], [2,4])    # 3 > 2 -> Swap O (list1 <-> list2)
            merge([4], [3,4])    # 4 > 3 -> Swap O (list1 <-> list2)
                merge([4], [4])    # 4 == 4 -> Swap X
                    merge([], [4])    # Return list2.
                    
                    return [4]
                return [4 -> 4]
            return [3 -> 4 -> 4]
        return [2 -> 3 -> 4 -> 4]
    return [1 -> 2 -> 3 -> 4 -> 4]
return [1 -> 1 -> 2 -> 3 -> 4 -> 4]    # Final answer.
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n + m)` Recursively processes both lists.
- Space Complexity: `O(n + m)` Recursion stack occupy extra space. 

---

## 🔥 Final Thoughts
Both approaches efficiently solve the `Merge Two Sorted Lists` problem in `O(n + m)`.  
Approach1 (iterative): More memory-efficient`O(1)`.  
Approach2 (recursive): Simpler and more intuitive, but uses extra space`O(n + m)`.   
It may cause issues when handling large dataset.
The iterative way is generally preferred and straightforward. Recursive approach is useful for understanding recursion concepts.


## References
[LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/description/)
