# 3Sum (LeetCode #15)
Given an integer array nums,  
return all the [nums[i], nums[j], nums[k]],  
`i != j`, `i != k`, `j != k`  
`nums[i] + nums[j] + nums[k] == 0`  

Solution set must not contain duplicate triplets.

**Constrains:**
> 3 <= nums.length <= 3000  
> -10^5 <= nums[i] <= 10^5

ex1:  
Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,-2],[-1,0,1]]

---

## Solution Approaches
### Approach 1: Brute Force
This approach iterates through all possible triplets using three different pointer `i`, `j`, `k`. 

**Code:** [Three sum - Brute Force](three_sum_brute_force.py)
```python
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # Needs a two number after `i`.
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k]  == 0:
                    results.append([nums[i], nums[j], nums[k]])
    return results
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n^3)` Three nested for loops, highly inefficient.
- Space Complexity: `O(n)` Sorting takes `O(n)`.

---

### Approach 2: Two Pointers(*Recommend*)
Explained the `i`, pointer(`right`, `left`)  
```
[-4, -2, -1, 0, 1, 2]
      i  ->        <-
          L        R
```

**Code:** [Three sum - Two Pointers](three_sum_twopointer.py)
```python
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                # Skip duplicate elements left and right.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                # Move pointers to find the next unique triplet
                left += 1
                right -= 1

    return results
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n^2)` The outer loop runs `O(n)`, and the inner two pointers runs`O(n)`.
- Space Complexity: `O(n)` Sorting takes `O(n)`.

---

## 🔥 Final Thoughts

Approach 1(Brute Force) `O(n^3)` Simple, straightforward but it occurs `Time Limit Exceeded` due to cubic time complexity.  
Approach 2(Two Pointers) `O(n^2)` Optimized by sorting and using a two pointer.  

Sorting helps by arranging negative numbers first.  
Allowing efficient pairing with positive numbers.  
The **Two Pointers** approach is the preferred solution for problem & better performance.

---

## References
[LeetCode #15](https://leetcode.com/problems/3sum/description/)