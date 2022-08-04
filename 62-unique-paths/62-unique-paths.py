class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create the bottom row of the grid
        row = [0 for _ in range(n)]
        row[-1] = 0
        for _ in range(m):
            new_row = [0 for _ in range(n)]
            for c in range(n - 1, -1, -1):
                if c == n - 1:
                    new_row[c] = 1
                else:
                    new_row[c] = new_row[c + 1] + row[c]
            row = new_row
        return row[0]
            
            
            
            
            
            
        
            
        