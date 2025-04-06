# Implement Queue using Stacks (LeetCode #232)
Implement a FIFO queue using only two stacks.  
The implemented queue should support all the functions(`push`, `peek`, `pop` and `empty`).

Implement the `MyQueue` class:  
`void push(int x)` Pushes element x to the back of the queue.  
`int pop()` Removes the element from the front of the queue and returns it.  
`int peek()` Returns the element at the front of the queue.  
`boolena empty()` Returns `true` if the queue is empty, `false` otherwise.

*Use only standard operations of a stack (`push to top`, `peek/pop from top`, `size`, and `is empty`).

**Constraints:**
> 1 <= x <= 9  
> At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.  
> All the calls to `pop` and `peek` are valid.

ex1:  
Input:  
["MyQueue", "push", "push", "peek", "pop", "empty"]  
[[ ], [1], [2], [ ], [ ], [ ]]  
Output:  
[null, null, null, 1, 1, false]

---

## Solution Approaches
### Approach 1: Lazy pop
**Code:** [Queue using Stacks - Lazy pop](queue_using_stacks_lazy_pop.py)
```python
def __init__(self):
    self.input = []
    self.output = []
    
def push(self, x: int) -> None:
    self.input.append()
    
def pop(self) -> int:
    self.peek()
    return self.output.pop()
    
def peek(self) -> int:
    if not self.output:
        while self.input:
            self.output.append(self.input.pop())
            
    return self.output[-1]

def empty(self) -> bool:
    return self.input == [] and self.output == []
```

#### ⏳ Time & Space Complexity
- Time Complexity: `Amortized O(1)` per operation - push is `O(1)`, pop/peek is `O(1)` amortized over many operations.
- Space Complexity: `O(n)` Uses two stacks to store all elements once.

---

### Approach 2: Eager pop
**Code:** [Queue using Stacks - Eager pop](queue_using_stack_eager_pop.py)
```python
def __init__(self):
    self.input = []
    self.output = []
    
def push(self, x: int) -> None:
    while self.input:
        self.output.append(self.input.append)
        
    self.input.append(x)
    
    while self.output:
        self.input.append(self.output.append)
    
def pop(self) -> int:
    return self.input.pop()

def peek(self) -> int:
    return self.input[-1]

def empty(self) -> bool:
    return not self.input
```

#### ⏳ Time & Space Complexity
- Time Complexity: `O(n)` for push (reordering stack every time), `O(1)` for pop and peek.
- Space Complexity: `O(n)` same, two stacks store all elements.

---

## 🔥 Final Thoughts
Both approaches correctly simulate a queue using only stack operations.  
Approach 1(Lazy pop) is more efficient in practice due to amortized `O(1)` performance and only transferring elements when needed(on `pop`/`peek`).  
Approach 2(Eager pop) shifts the cost every `push`, ensuring `pop` and `peek` are always `O(1)`. While logically valid, it's less practical due to repeated stack reordering.

Thus, **Lazy pop** is the preferred and widely used solution.

---

## Lazy vs Eager Strategy
> Lazy and Eager are two contrasting strategies used to control when a computation or operation should be performed.  
> Used in stack<->queue problems for deciding **when to transfer data**. (Not only for this solution)

### Lazy Pop
Delay the work until it's absolutely needed.  
- Pros: Efficient for large data, avoids unnecessary computation.
- Common in:
    - Used in `pop()` or `peek()` logic.  
    - Good for when `push()` is frequent.
    - Segment Tree Lazy Propagation.
    - On-demand caching/LRU cache.

### Eager Pop
Do the work as early as possible to make later access fast.
- Pros: Fast queries after upfront work.
- Common in:
    - Prepare early (on `push`), `pop()` and `peek()` are fast.
    - Good for when `pop()` is frequent and performance-critical.
    - Prefix sum.
    - Preprocessing in dynamic programming or graphs.

### Final Note
Lazy and Eager **is not** just a data structure trick.  
It is a general **algorithm design mindset**.  
Thinking of it as choosing where to pay the cost, **now (eager)** or **later (lazy)**.

## References
[LeetCode #232](https://leetcode.com/problems/implement-queue-using-stacks/description/)