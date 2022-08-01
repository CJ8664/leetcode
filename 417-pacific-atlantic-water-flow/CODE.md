```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac_plots, atl_plots = set(), set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def search(r, c, prev_height, plots):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or (r, c) in plots: return
            if heights[r][c] < prev_height: return
            
            plots.add((r, c))            
            for nr, nc in dirs:
                search(r + nr, c + nc, heights[r][c], plots)
        
        # Get plots which reach atlantic and pacific backwards
        # from verticals
        for r in range(ROWS):
            search(r, 0, -1, pac_plots)
            search(r, COLS - 1, -1, atl_plots)
            
        # Get plots which reach atlantic and pacific backwards
        # from verticals
        for c in range(COLS):
            search(0, c, -1, pac_plots)
            search(ROWS - 1, c, -1, atl_plots)
        
        # Return the set of elements that can be reached 
        # from both pacific and atlantic
        return (pac_plots & atl_plots)
        
```
