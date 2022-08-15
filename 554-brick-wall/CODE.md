```python
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Init the dict with default values for the case where there is only
        # one brick in each row of the wall
        gap_count = {0: 0}
        for row in wall:
            gap = 0
            for brick in row[:-1]:
                gap += brick
                gap_count[gap] = 1 + gap_count.get(gap, 0)
        return len(wall) - max(gap_count.values())
                
            
            
            
        
        
```
