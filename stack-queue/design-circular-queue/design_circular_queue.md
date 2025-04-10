# Design Circular Queue (LeetCode #622)
The circular queue is linear data structure based on FIFO principle.  
The last position is connected back to the first position to make a circle.  
It is also called "Ring Buffer".

One of the benefits of the circle queue is that we can make use of the spaces in front of the queue.  
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue.  
But using the circular queue, we can use the space to store new value.

Implement the `MyCircularQueue` class:  
- `MyCircularQueue(k)` Initialized the object with the size of the queue to be `k`.  
- `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.
- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.
- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.
- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.
- `boolean isEmpty()` Checks whether the circular queue is empty or not.
- `boolean isFull()` Checks whether the circular queue is full or not.

**Constraints:**
> `1 <= k <= 1000`  
> `0 <= value <= 1000`  
> At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.

ex1:  
Input:  
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]  
[[3], [1], [2], [3], [4], [ ], [ ], [ ], [4], [ ]]  
Output:  
[null, true, true, true, false, 3, true, true, true, 4]

---

## Solution Approaches
### Pseudo Code

enQueue(val)
```psudo
If the queue is full:
    return False
    
Insert val at rear position
Move rear to (rear + 1) % capacity
Increase size
Return True
```

deQueue()
```psudo
If the queue is empty:
    return False
    
Move front to (front + 1) % capacity
Decrease size
Return True
```

Front()
```psudo
If the queue is empty:
    return -1
    
Return queue[front]
```

Rear()
```psudo
If the queue is empty:
    return -1
    
Return queue[(rear - 1 + capacity) % capacity]
```

isEmpty()
```psudo
Return size == 0
```

isFull()
```psudo
Return size == capacity
```

---

### Approach 1: Two pointers(Recommended)
**Code:** [Design Circular Queue - Two pointers](design_circular_queue_two_pointers.py)
```python
def __init__(self, k: int):
    self.q = [None] * k
    self.max_len = k
    self.front = 0
    self.rear = 0
    self.size = 0

# Move the rear pointer — always points to the next position to insert.
def enQueue(self, value: int) -> bool:
    if self.isFull():
        return False
    
    self.q[self.rear] = value
    self.rear = (self.rear + 1) % self.max_len
    self.size += 1
    return True

# Move the front pointer — always points to the next position to remove.
def deQueue(self) -> bool:
    if self.isEmpty():
        return False
    
    self.front = (self.front + 1) % self.max_len
    self.size -= 1
    return True

def Front(self) -> int:
    if self.isEmpty():
        return -1
    return self.q[self.front]

def Rear(self) -> int:
    if self.isEmpty():
        return -1
    
    return self.q[(self.rear - 1 + self.max_len) % self.max_len]

def isEmpty(self) -> bool:
    return self.size == 0

def isFull(self) -> bool:
    return self.size == self.max_len
```

---

### Example Walkthrough
```
Input:

MyCircularQueue circularQueue = new MyCircularQueue(5);
circularQueue.enQueue(10);
circularQueue.enQueue(20);
circularQueue.Rear();
circularQueue.deQueue();
circularQueue.Front();
```

init:  
rear = 0    
front = 0  
self.q = [None, None, None, None, None]  
self.max_len = 5  

**circularQueue.enQueue(10)**
> self.q[0] = 10,  
> self.rear = (0 + 1) % 5, self.rear = 1  
> self.size = 1  
> q = [10, None, None, None, None]

---

init:  
rear = 1    
front = 0  
self.q = [10, None, None, None, None]  
self.max_len = 5

**circularQueue.enQueue(20)**
> self.q[1] = 20,  
> self.rear = (1 + 1) % 5, self.rear = 2  
> self.size = 2  
> q = [10, 20, None, None, None]

---

init:  
rear = 2    
front = 0  
self.q = [10, 20, None, None, None]  
self.max_len = 5

**circularQueue.Rear()**
> self.isEmpty(), self.size = 2 -> False  
> self.q[(2 - 1 + 5) % 5] -> self.q[1], return 20

---

init:  
rear = 2    
front = 0  
self.q = [10, 20, None, None, None]  
self.max_len = 5

circularQueue.deQueue()
> self.front = (0 + 1) % 5, self.front = 1
> self.size = 1

`self.q[0] = 10` is still physically exists.  
But the front pointer is move forward.  
So `self.q[0]` is not valid data anymore.

---

init:  
rear = 2    
front = 1  
self.q = [10, 20, None, None, None]  
self.max_len = 5

circularQueue.Front()  
> self.q[1] = 20

---

#### ⏳ Time & Space Complexity
- Time Complexity: All operations `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull` takes `O(1)` time.
- Space Complexity: Uses `O(k)` space for storing elements and managing pointers.

---

### Approach 2: Linked List
**Code:** [Design Circular Queue - Linked list](design_circular_queue_linked_list.py)
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        # head, tail are reference the Node. -> None
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        new_node = Node(value)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.head = self.head.next
        self.size -= 1

        if self.size == 0:
            self.tail = None

        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
```

### Example Walkthrough
```
Input:

MyCircularQueue circularQueue = new MyCircularQueue(5);
circularQueue.enQueue(10);
circularQueue.enQueue(20);
circularQueue.deQueue();
```

init:  
capacity = 5  
size = 0  
head = None  
tail = None  

**circularQueue.enQueue(10)**  
> new_node = Node(10)  
> self.size == 0 -> so, head,tail -> Node(10)
> size = 1

```
head -> 10
        tail
```

---

init:  
capacity = 5  
size = 1  
head = Node(10)  
tail = Node(10)

**circularQueue.enQueue(20)**
> new_node = Node(20)
> else: tail.next = Node(20)
```
head -> 10 -> 20
```
> tail = Node(20)
```
head -> 10 -> 20
              tail
```
> size = 20

---

init:  
capacity = 5  
size = 2  
head = Node(10)  
tail = Node(20)

---

**circularQueue.deQueue()**  
head = head.next means move forward the pointer.  
So,
```
head -> 20
tail -> 20
```
size = 1

---

#### ⏳ Time & Space Complexity
- Time Complexity: All operations `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull` takes `O(1)` time.
- Space Complexity: Uses `O(k)` space to store up to k linked nodes.

---

## 🔥 Final Thoughts
Approach 1(Two pointers) uses two pointers(`front`, `rear`) and a size counter to simulate a ring buffer. Ideal for fixed-size queues.  
Approach 2(Linked List) more flexible in dynamic memory usage, though slightly more complex.  
It efficiently works all queue operations in `O(1)` time using constant space.  

---

## References
[LeetCode #622](https://leetcode.com/problems/design-circular-queue/description/)