# Daily Temperatures (LeetCode #739)
Given an array of integers `temperatures`.  
Return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature.  
If there is no future day(possible), keep `answer[i] == 0` instead.

**Constraints:**
>`1 <= temperatures.length <= 10^5`  
>`30 <= temperatures[i] <= 100`

ex1:  
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]  
Output: [1, 1, 4, 2, 1, 1, 0, 0]

---

## Solution Approaches
### Approach 1: Stack
**Code:** [Daily Temperatures - Stack](daily_temperatures_stack.py)
```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []

    # enumerate(temperatures) -> (index, value), unpacking i for index, cur for value.
    for i, cur in enumerate(temperatures):
        # If cur temp is higher than top of the stack temp -> Found the answer.
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()    # Pop the lower temp,
            answer[last] = i - last    # Save the diff between index i and lower temp.
            
        # If it couldn't find the high temp, push the index.
        stack.append(i)
        
    return answer
```

### Example Walkthrough
```
Input: [73, 74, 75, 71, 69, 72, 76, 73]
Index:   0   1   2   3   4   5   6   7  
answer: [0, 0, 0, 0, 0, 0, 0, 0]
```

>i = 0, cur = 73 -> skip the while loop, stack: [0]  

>i = 1, cur = 74  
while loop, 74 > temperatures[0],  
stack.pop() -> last = 0,  
answer[0] = 1 - 0 -> stack: [1], answer: [1, 0, 0, 0, 0, 0, 0, 0]  

>i = 2, cur = 75  
while loop, 75 > temperatures[1],  
stack.pop() -> last = 1,  
answer[1] = 2 - 1 -> stack: [2], answer: [1, 1, 0, 0, 0, 0, 0, 0]  

>i = 3, cur = 71  
while loop, 71 < temperatures[2] -> skip the while loop, stack: [2, 3]  

>i = 4, cur = 69  
while loop, 69 < temperatures[3] -> skip the while loop, stack: [2, 3, 4]  

>i = 5, cur = 72, stack: [2,3,4]   
while loop, 72 > temperatures[4],  
stack.pop() -> last = 4
answer[4] = 5 - 4  
while loop, 72 > temperatures[3],
stack.pop() -> last = 3  
answer[3] = 5 - 3  
while loop, 72 < temperatures[2], loop end.
stack: [2, 5], answer: [1, 1, 0, 2, 1, 0, 0, 0]

...  
Final Output: [1, 1, 4, 2, 1, 1, 0, 0]

---

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Each temperature index is pushed and pooped from the stack.
- Space Complexity: `O(n)` Stack stores indices in the worst case.

---

### Approach 2: Jump Table
**Code:** [Daily Temperatures - Jump Table](daily_temperatures_jump_table.py)
```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n

    # for (start, end, step)
    for i in range(n - 2, -1, -1):
        next_day = i + 1
        while next_day < n and temperatures[i] >= temperatures[next_day]:
            if answer[next_day] == 0:    # If no warmer day exists after next_day, break.
                break
                
            next_day += answer[next_day]    # Jump to the next warmer day.

        if next_day < n and temperatures[i] < temperatures[next_day]:
            answer[i] = next_day - i    # Calculate how many days to wait.

    return answer
```

### Example Walkthrough
```
Input: [73, 74, 75, 71, 69, 72, 76, 73]  
n: 8  
answer: [0, 0, 0, 0, 0, 0, 0, 0]
```  

>i = 6 -> temperatures[6] = 76  
while loop,  
7 < 8 and 76 >= 73,  
answer[7] == 0 -> break.  
if 7 < 8 and 76 < 73 -> False.  

>i = 5 -> temperatures[5] = 72  
while loop,  
6 < 8 and 72 >= 76 -> break.  
if 6 < 8 and 72 < temperatures[6]:  
answer[5] = 6 - 5  
-> answer: [0, 0, 0, 0, 0, 1, 0, 0]  

>i = 4 -> temperatures[4] = 69  
while loop,  
5 < 8 and 69 >= temperatures[5] -> break.  
if 5 < 8 and 69 < temperatures[5]:  
answer[4] = 5 - 4  
-> answer: [0, 0, 0, 0, 1, 1, 0, 0]

>i = 3 -> temperatures[3] = 71  
while loop,  
4 < 8 and 71 >= temperatures[4],  
if answer[4] == 0 -> False.  
next_day += answer[4] -> next_day = 5  
while loop,  
5 < 8 and 71 >= temperatures[5] -> break.  
if 5 < 8 and 71 < temperatures[5]:  
answer[3] = 5 - 3  
-> answer: [0, 0, 0, 2, 1, 1, 0, 0]  

...  
Final Output: [1, 1, 4, 2, 1, 1, 0, 0]

---

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` Each index is processed once, and jumps skip over unnecessary checks.
- Space Complexity: `O(1)` The result list is counted as output space, no extra stack or list.

---

## 🔥 Final Thoughts
Both approaches solve the `Daily Temperatures` efficiently in linear time `O(n)`.  
Approach 1(Stack) is a monotonic decreasing stack to track. Intuitive and simple but uses extra space (stack).  
Approach 2(Jump Table) uses previous answer to quickly skip. Reduces unnecessary checks but trickier to implement.

The Monotonic decreasing stack pattern is widely used to solve problems.  
On the other hand, the jump table approach is an efficient optimization technique and is worth understanding to deepen algorithmic thinking.

---

## References
[LeetCode #739](https://leetcode.com/problems/daily-temperatures/)