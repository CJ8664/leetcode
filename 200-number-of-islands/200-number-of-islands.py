class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def sink_island(r, c):
            if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
                return
            if grid[r][c] == "0":
                return 
                
            grid[r][c] = "0"
            for nr, nc in dir:
                sink_island(r + nr, c + nc)
        
        num_isle = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    num_isle += 1
                    sink_island(r, c)
                    
        return num_isle
                    
        