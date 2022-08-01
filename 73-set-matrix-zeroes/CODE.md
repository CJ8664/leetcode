```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f_row_zero = f_col_zero = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0
                    if row == 0:
                        f_row_zero = True
                    if col == 0:
                        f_col_zero = True
        
        # Update everything except first row and col
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if f_row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
                
        if f_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
```
