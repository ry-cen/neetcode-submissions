class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            match token:
                case "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)
                case "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                case "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 * num2)
                case "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 / num1))
                case _:
                    stack.append(int(token))

        return stack[0]