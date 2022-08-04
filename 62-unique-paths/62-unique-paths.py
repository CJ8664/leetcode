class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 0
        dirs = [(0, 1), (1, 0)]
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[m - 1][n - 1] = 1
        
        for r in range(m - 1, -1 , -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                if c == n - 1:
                    grid[r][c] = grid[r + 1][c]
                elif r == m - 1:
                    grid[r][c] = grid[r][c + 1]
                else:
                    grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
                
        for row in grid:
            print(row)
                
        return grid[0][0]
            
            
            
            
            
            
        
            
        