```python
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.curr_min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append((val, self.curr_min))
        self.curr_min = min(self.curr_min, val)
        

    def pop(self) -> None:
        _, self.curr_min = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.curr_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
