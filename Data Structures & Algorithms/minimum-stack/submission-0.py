class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.ministack.append(min(val, self.ministack[-1]) if self.ministack else val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.ministack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
        
