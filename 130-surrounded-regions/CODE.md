```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_r, n_c = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def mark_border_regions(r, c):
            if not (0 <= r < n_r) or not (0 <= c < n_c):
                return
            if board[r][c] in {"X", "#"}:
                return 

            board[r][c] = "#"
            for d_r, d_c in dirs:
                mark_border_regions(r + d_r, c + d_c)
        
        # Find all the border conneected regions
        for r in range(n_r):
            mark_border_regions(r, 0)
            mark_border_regions(r, n_c -1)
        for c in range(n_c):
            mark_border_regions(0, c)
            mark_border_regions(n_r - 1, c)
            
        # Flip all non border regions and also restore border regions
        for r in range(n_r):
            for c in range(n_c):
                if board[r][c] == "O": board[r][c] = "X"
                if board[r][c] == "#": board[r][c] = "O"   
            
                
        
```
