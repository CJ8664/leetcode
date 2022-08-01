```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l, r = 0, 0
        result = 0
        while r < len(s):
            # Store how many characters for each alphabet
            char_freq[s[r]] += 1
            # Cannot make substitution
            while (r - l + 1) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result
                
                
                
            
            
        
        
                
                
            
            
        
```
