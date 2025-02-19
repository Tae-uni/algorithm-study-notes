# Reorder Log Files (LeetCode #937)

The first word is the `identifier`.  
Letter-logs: Lowercases Eng letters.  
Digit-logs: digits.

Letter come before all digit.  
Ordered by contents. If contents are the same, ordered by identifier.  
**Return the final order of the logs.**

**Constrains:**
> 1 <= logs.length <= 100  
> 3 <= logs[i].length <= 100  
> logs[i] separated by a single space.

ex1:  
Input: logs = ["dig1 8 1 5 1","let1 art can", "dig2 3 6","let2 own kit dig","let3 art zero"]  
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]  

---

## Solution Approaches
### Way 1: Separate lists & sorting (Recommended)
**Code:** [Reorder_Log with Lambda](reorder_log_lambda.py)

```python
def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
    # [1:], Sort by content
    # [0], If same content, sort by identifier
    return letters + digits
```

### Way 2: Sorted (*More Pythonic*)
**Code:** [Reorder Log](reorder_log.py)

```python
def reorderLogFiles(logs: List[str]) -> List[str]:
    def sorting_algorithm(log):
        left, right = log.split(" ", 1)
        if log[-1].isdigit():
            return (1,) # Put the digit at the end.
        # Sort letter logs by content first, identifier.
        return (0, right, left)

    return sorted(logs, key=sorting_algorithm)
```

## 🔥 Final Thoughts
Both approaches have the same Time Complexity of `O(nlogn*m)`. Cause, they rely on sorting operations.  
Otherwise, when it comes to Space Complexity, Way1 (Separate Lists & Sorting) is more efficient, requiring `O(m+n)`.  
Way2 (Using sorted()) has a higher space overhead of `O(mlogn)`.  
Thus, Way 1 is better for large inputs as it optimizes memory usage.
---
## References
- [Reorder Log Files](https://leetcode.com/problems/reorder-data-in-log-files/description/)
- [Python String isdigit() Method](https://www.w3schools.com/python/ref_string_isdigit.asp)