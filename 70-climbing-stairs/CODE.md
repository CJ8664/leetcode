```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        second_last_step, last_step = 1, 2
        # For a given postion you can reach it by 
        # 1 step + number of way you reached last step
        # 2 step + number of way you reached second last step
        # 1 and 2 are possible moves given in question hence the equation
        for _ in range(3, n + 1):
            second_last_step, last_step = last_step, (second_last_step + last_step)
        return last_step
            
        
```
