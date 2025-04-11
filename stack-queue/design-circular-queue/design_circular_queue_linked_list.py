class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
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