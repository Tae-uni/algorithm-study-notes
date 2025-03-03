# Array Partition (LeetCode #561)
Input is always `n` pairs of integer.  
Return the *maximized* sum of min of pair.

**Constraints:**
> 1 <= n <= 10^4  
> nums.length == 2 * n  
> -10^4 <= nums[i] <= 10^4

ex1:  
Input: nums = [1,4,3,2]  
Output: 4

---

## Solution Approaches
### Approach 1: Ascending
**Code:** [Array Partition - Ascending](array_partition_ascending.py)

```python
def arrayPairSum(nums: List[int]) -> int:
    total = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            total += min(pair)
            pair = []

    return total
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(nlogn)` Sorting takes `O(nlogn)`, iterating takes `O(n)`. 
- Space Complexity: `O(1)` Uses only a few extra variables.

---

### Approach 2: Even Index Sum
**Code:** [Array Partition - Even](array_partition_even.py)

```python
def arrayPairSum(nums: List[int]) -> int:
    total = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            total += n

    return total
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(nlogn)` Sorting takes `O(nlogn)`, iterating takes `O(n)`.
- Space Complexity: `O(1)` No additional space expect.

---

### Approach 3: Optimized (Pythonic)
**Code:** [Array Partition - Optimized](array_partition_optimized.py)
```python
def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    # Sum every second element (min of each pair)
    return sum(nums[::2])
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(nlogn)` Sorting takes `O(nlogn)`, slicing takes `O(n)`.
- Space Complexity: `O(n)` **sorted(nums)** creates a new list.

---

## 🔥 Final Thoughts

All three approaches share the same `O(nlogn)` time complexity due to sorting.  
However, approach 1 and 2 use `O(1)` space. Making them more efficient in memory.  
Approach 3 is the simplest and pythonic but requires extra `O(n)` space.  
Approach 2 is the best way to solve this problem.

---

## References
[LeetCode #561](https://leetcode.com/problems/array-partition/description/)