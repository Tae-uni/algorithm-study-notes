# Product of Array Except Self (LeetCode #238)
Given an integer array `nums`,  
Return an array `answer`, answer[i] is equal to the all product of all element expect nums[i].  
**`O(n)` Time, without using division operation.**

**Constraints:**
> 2 <= nums.length <= 10^5  
> -30 <= nums[i] <= 30  
> The input is generated answer[i] fit in 32-bit integer.

ex1:  
Input: nums = [1,2,3,4]  
Output: [24,12,8,6]

---

## Solution Approaches
### Approach 1: Optimized(Recommend)
**Code:** [Product Except Self - Optimized](product_except_self_optimized.py)
```python
def productExceptSelf(nums: List[int]) -> List[int]:
    # `1` doesn't affect a result of multiplication.
    # `1 * n` is n.
    output = [1] * len(nums)
    
    left = 1
    # Left Pass(Loop)
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]
        
    right = 1
    # Right Pass(Loop)
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Iterate through the array twice, prefix and suffix.
- Space Complexity: `O(1)` Use a few variables.

---

### Approach 2: Extra Space
**Code:** [Product Except Self - Extra Space](product_except_self_extra.py)
```python
def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1

    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Iterate through the array twice, prefix and suffix.
- Space Complexity: `O(n)` Extra storage, due to the additional array(`out`).

---

## 🔥 Final Thoughts
Both approaches efficiently solve the problem through the same core ideas`O(n)`.  
Iterate **left to right** and **right to left**, leveraging `1` as a multiplier.

Approach 1 is the best way to solve it. No extra memory usage `O(1)` space.  
Approach 2 is uses extra arrays, leading to `O(n)` space complexity.  

## References
[LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/description/)