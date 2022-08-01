```python
class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
    
    
        # DFS + Memoization
        memory = {len(s): 1}
        def helper(idx):
            if idx in memory:
                return memory[idx]
            if s[idx] == "0":
                return 0
            res = helper(idx + 1)
            if idx + 1 < len(s) and int(s[idx:idx + 2]) <= 26:
                res += helper(idx + 2)
            memory[idx] = res
            return res
        return helper(0)
                

        
```
