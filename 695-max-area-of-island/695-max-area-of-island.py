class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def sink_island(r, c):
            if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
                return 0
            if grid[r][c] == 0:
                return 0
                
            grid[r][c] = 0
            area = 1
            for nr, nc in dir:
                area += sink_island(r + nr, c + nc)
            return area
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, sink_island(r, c))
                    
        return max_area
                    
        