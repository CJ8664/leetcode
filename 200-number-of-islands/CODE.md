```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def sink(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] != "1": 
                return
            # sink the part of island
            grid[r][c] = "0"
            for nr, nc in dirs:
                sink(r + nr, c + nc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    result += 1
                    sink(r, c)
        return result

        
```
