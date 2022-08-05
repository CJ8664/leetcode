```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create the bottom row of the grid
        row = [0 for _ in range(n)]
        # The last element in the last row represents the 
        # target. We can reach there in 1 way
        row[-1] = 0
        
        # We have to compute every row of the grid starting 
        # from the bottom
        for _ in range(m):
            new_row = [0 for _ in range(n)]
            for c in range(n - 1, -1, -1):
                # There is only one way to reach the target
                # from the last column that is to keep
                # going down
                if c == n - 1:
                    new_row[c] = 1
                # For any other position in the grid
                # We can go right OR go down. So from here
                # The total number of way is
                # num_way(down) + num_ways(right)
                else:
                    new_row[c] = new_row[c + 1] + row[c]
            row = new_row
        return row[0]
            
            
            
            
            
            
        
            
        
```
