```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Tracks the last position from the right side at which we can reach
        # the last index of array
        goal = len(nums) -1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
            
                
            
                
                
        
```
