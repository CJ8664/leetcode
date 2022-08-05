```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result, i = [], 0
        ROWS, COLS, total = len(matrix), len(matrix[0]), len(matrix) * len(matrix[0])
        
        for i in range(ROWS):
            for c in range(i, COLS - i) :
                result.append(matrix[i][c])
                if len(result) == total: return result

            for r in range(i + 1, ROWS - i):
                result.append(matrix[r][COLS - 1 - i])
                if len(result) == total: return result
            
            for c in range(COLS - 2 - i, -1 + i , -1):
                result.append(matrix[ROWS - 1 - i][c])
                if len(result) == total: return result
    
            for r in range(ROWS - 2 - i, -1 + i + 1, -1):
                result.append(matrix[r][i])
                if len(result) == total: return result
            
        return result
        
        
```
