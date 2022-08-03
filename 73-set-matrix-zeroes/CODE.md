```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero, first_col_zero = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r == 0: first_row_zero = True
                    if c == 0: first_col_zero = True
                    matrix[r][0], matrix[0][c] = 0, 0

        # Update everything except first row and col
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                    
            
        
```
