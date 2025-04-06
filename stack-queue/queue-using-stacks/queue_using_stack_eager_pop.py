class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        while self.input:
            self.output.append(self.input.pop())

        self.input.append(x)

        while self.output:
            self.input.append(self.output.pop())

    def pop(self) -> int:
        return self.input.pop()

    def peek(self) -> int:
        return self.input[-1]

    def empty(self) -> bool:
        return not self.input