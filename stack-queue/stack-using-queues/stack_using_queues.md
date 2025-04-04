# Implement Stack using Queues (LeetCode #225)
Implement a LIFO stack using only two queues.  
The implemented stack should support all the functions of normal stack(`push`, `top`, `pop`, and `empty`).  

Implement the `MyStack` class:  
`void push(int x)` Pushes element x to the top of the stack.  
`int pop()` Removes the element on the top of the stack, returns it.  
`int top()` Returns the element on the top of the stack.  
`boolean empty()` Returns `true` if the stack is empty, `false` otherwise.  

*Use only standard operations of a queue (`push to back`, `peek/pop from front`, `size`, `is empty`).

**Constraints:**
> `1 <= x <= 9`  
> At most `100` calls will be made to `push`, `pop`, `top` and `empty`.  
> All the calls to `pop` and `top` are valid.

ex1:  
Input:  
["MyStack", "push", "push", "top", "pop", "empty"]  
[[ ], [1], [2], [ ], [ ], [ ]]  
Output:  
[null, null, null, 2, 2, false]

## Solution Approaches
### Approach 1: Eager pop
**Code:** [Stack using queues - Eager pop](stack_using_queues_eager_pop.py)
```python
def __init__(self):
    self.q = deque()

def push(self, x: int) -> None:
    self.q.append(x)
    for _ in range(len(self.q) - 1):
        self.q.append(self.q.popleft())

def pop(self) -> int:
    return self.q.popleft()

def top(self) -> int:
    return self.q[0]

def empty(self) -> bool:
    return len(self.q) == 0
```

#### ⏳ Time & Space Complexity
- Time Complexity: 
- Space Complexity:

---

### Approach 2: Lazy pop
**Code:** [Stack using queues - Lazy pop](stack_using_queues_lazy_pop.py)
```python
def __init__(self):
    self.q1 = deque()
    self.q2 = deque()

def push(self, x: int) -> None:
    self.q2.append(x)

def pop(self) -> int:
    while len(self.q1) > 1:
        self.q2.append(self.q1.popleft())
    res = self.q1.popleft()
    self.q1, self.q2 = self.q2, self.q1
    return res

def top(self) -> int:
    while len(self.q1) > 1:
        self.q2.append(self.q1.popleft())
    res = self.q1.popleft()
    self.q2.append(res)
    self.q1, self.q2 = self.q2, self.q1
    return res

def empty(self) -> bool:
    return not self.q1
```

#### ⏳ Time & Space Complexity
- Time Complexity:
- Space Complexity:

---

## 🔥 Final Thoughts

---

## References
[LeetCode #225](https://leetcode.com/problems/implement-stack-using-queues/description/)