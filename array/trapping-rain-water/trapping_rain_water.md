# Trapping Rain Water (LeetCode #42)
`n` non negative integers.  
It is representing an elevation map where the width of each bar is 1,  
compute how much water it can trap after raining.

**Constraints:**
> n == height.length  
> 1 <= n <= 2 * 10^4  
> 0 <= height[i] <= 10^5

ex1:  
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  
Output: 6

![Rain water trap img](rainwatertrap.png)

---

## Solution Approaches
### Approach 1: Two Pointers
**Code:** [Trapping Rain Water - Two Pointers](trapping_rain_twopointer.py)
```python
def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    water = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)
        
        if left <= right:
            water += left_max - height[left]
            left += 1
        else:
            water += right_max - height[right]
            right -= 1
            
    return water
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` The left and right pointers traverse the entire list once.
- Space Complexity: `O(1)` No additional data.

---

### Approach 2: Stack
The trapped water determined by the width(distance) between boundaries and height difference of water level.  
**Code:** [Trapping Rain Water - Stack](trapping_rain_stack.py)
```python
def trap(height: List[int]) -> int:
    stack = []
    volume = 0
    
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            
            if not len(stack):
                break
                
            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]
            
            volume += distance * water
        stack.append(i)
    return volume
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Each element is pushed and popped from the stack at most once.
- Space Complexity: `O(n)` Stack stores the indices, requiring extra space in the worst case.

---

## 🔥 Final Thoughts
Both approaches run in `O(n)`. Good way to solve **Trapping Rain Water**.  
The only difference is Space Complexity.  
- Approach 1(Two Pointers): `O(1)` space, memory efficiency. It maintains two boundaries(left_max, right_max) and moves the pointer.  
- Approach 2(Stack): `O(n)` space, stack storing indices. It is useful for dynamically handling elevation changes.

The Two Pointers approach is simpler, more intuitive due to constant space usage.  
However, the Stack approach provides an alternative perspective(height comparisons, boundary tracking).

## References
- [LeetCode #42](https://leetcode.com/problems/trapping-rain-water/description/)
- [Monotonic Stack](https://www.geeksforgeeks.org/introduction-to-monotonic-stack-2/)