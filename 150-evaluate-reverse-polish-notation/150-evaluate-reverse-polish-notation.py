class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
                continue
            # print(stack)
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        return stack[0]
        