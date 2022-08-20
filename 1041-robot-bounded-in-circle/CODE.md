```python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_x, dir_y, x, y = 0, 1, 0, 0
       
        for ins in instructions:
            if ins == "G":
                x, y = x + dir_x, y + dir_y
            if ins == "L":
                dir_x, dir_y = -1 * dir_y, dir_x
            if ins == "R":
                dir_x, dir_y = dir_y, -1 * dir_x
            
        return (x, y) == (0, 0) or (dir_x, dir_y) != (0, 1)
                
            
        
```
