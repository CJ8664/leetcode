```python
class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            "}": "{", 
            ")": "(",
            "]": "[",
        }
        stack = deque()
        for par in s:
            if par not in par_map:
                stack.append(par)
            elif par in par_map and len(stack) > 0 and stack[-1] == par_map[par]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
                
                
        
```
