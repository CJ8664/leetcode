```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        # Check if the string bound by given indexes is palindrome
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def dfs(i):
            # if we have reached the end of string to find partitions
            if i >= len(s):
                res.append(part.copy())
                return
            # for i = 0 get substring 0:1, 0:2, 0:3...
            # If that string is palindrome, recurisively check if any of 
            # its substring is palindorme
            for j in range(i, len(s)):
                if isPali(i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    # before this is poped recurison base comdtion will be hit
                    # and the result will be preserved
                    part.pop()
        dfs(0)
        return res
```
