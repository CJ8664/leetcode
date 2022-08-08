```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Gather the characters and their freq in dict for s1
        s1_counter = Counter(s1)
        # Gather the characters and their freq in dict from s2 
        # for the first len(s1) characters in s2
        s2_counter = Counter(s2[:len(s1)])
        
        if s1_counter == s2_counter:
            return True
        
        l, r = 0, len(s1)
        while r < len(s2):
            # Add right character to window
            s2_counter[s2[r]] += 1
            # Decrement left character from window
            s2_counter[s2[l]] -= 1
            # If no character left in current window, pop
            if s2_counter[s2[l]] == 0:
                s2_counter.pop(s2[l])
                
            # If the window character and their freq matches
            # return true
            if s1_counter == s2_counter:
                return True
            # slide the window
            l, r = l + 1, r + 1
        return False
            
            
        
        
```
