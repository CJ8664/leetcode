```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Consider the 2D matrix to be a flat 1D array
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, len(matrix[0]))
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
```
