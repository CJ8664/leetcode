```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) > len(t):
            small, big = t, s
        else:
            small, big = s, t
        chars = {}
        for c in small:
            chars[c] = 1 + chars.get(c, 0)
            
        for c in big:
            if c not in chars or chars[c] == 0:
                return False
            chars[c] -= 1
        return True
            
                
        
            
        
```
