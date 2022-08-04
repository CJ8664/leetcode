class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]
        for _ in range(m - 1):
            new_row = [0 for _ in range(n)]
            for c in range(n - 1, -1, -1):
                if c == n - 1:
                    new_row[c] = 1
                else:
                    new_row[c] = new_row[c + 1] + row[c]
            row = new_row
        return row[0]
            
            
            
            
            
            
        
            
        