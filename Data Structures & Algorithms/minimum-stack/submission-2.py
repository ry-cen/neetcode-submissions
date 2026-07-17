class MinStack:

    def __init__(self):
        self.stack = deque()
        self.ministack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.ministack.append(min([val, self.ministack[-1] if self.ministack else float('inf')]))

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
        
