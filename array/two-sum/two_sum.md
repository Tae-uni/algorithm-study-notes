# Two Sum (LeetCode #1)
Array of int `nums` and an integer `target`.  
Return the answer in any order.  

**Constraints:**  
> 2 <= nums.length <= 10^4  
> -10^9 <= nums[i] <= 10^9  
> -10^9 <= target <= 10^9  
> Only one valid answer exists.

ex1:  
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]

ex2:  
Input: nums = [3, 2, 4], target = 6  
Output: [1, 2]

---

**Note:**  
What is Brute Force?  
A straightforward method that tries all possible solutions one by one until finds the right answer,  
but often inefficient due to its high time complexity.

---

## Solution Approaches
### Approach 1: Brute Force
**Code:** [Two sum - Brute Force](two_sum_brute_force.py)
```python
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n^2)` Check all possible pairs of numbers using a nested loop.
- Space Complexity: `O(1)` No extra space is used.

---

### Approach 2: HashMap
**Code:** [Two sum - HashMap](two_sum_hashmap.py)
```python
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    """
        enumerate() : Returns the index and value as a tuple. (num=key, index=value)
        {2: 0}
        {2: 0, 7: 1}
        {2: 0, 7: 1, 11: 2}
        {2: 0 ,7: 1, 11: 2, 15: 3}
    """
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        # Check if the complement (target - num) exists in the map and ensure it is not the same index.
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]] # Expect [0, nums_map[9 - 2]] -> [0, 1]
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` - Each element is processed once, linear time.
- Space Complexity: `O(n)` - A dictionary stores up to n elements in the worst case.

---

### Approach 3: Optimized HashMap
**Code:** [Two sum - Optimized](two_sum_optimized.py)
```python
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i] # Return indices in correct order.
        nums_map[num] = i # Store the current number and index.
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` - Iterate through the list once.
- Space Complexity: `O(n)` - Store each number in a dictionary.

---

## 🔥 Final Thoughts
Approach 1(Brute Force): `O(n^2)`, simple but inefficient for large datasets.  
Approach 2(Dictionary Lookup - HashMap): Improves efficiency to `O(n)` using the HashMap. But still requires two loops.  
Approach 3(Optimized HashMap): Time complexity is same with Approach 2, but refactored code to one loop.  

I also considered solving this problem through the `Two Pointer`.   
However, I realized that if `nums` is not sorted cannot be applied.

## References
- [LeetCode #1](https://leetcode.com/problems/two-sum/)
- [Brute Force](https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/)
- [enumerate()]()