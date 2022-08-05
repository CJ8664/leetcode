```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Store the result, +1 is the base case where
        # we have broken down everything in the string s
        # and our index entered next iteration of loop
        result = [False for _ in range(len(s) + 1)]
        result[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            # For every word in the dict
            for w in wordDict:
                # If the dict word matches the substring from 
                # this point to the right and the string after
                # that can be broken down then mark this 
                # index also that from here the string can be 
                # broken down
                if s[i: i + len(w)] == w and result[i + len(w)]:
                    result[i] = True
        return result[0]
```
