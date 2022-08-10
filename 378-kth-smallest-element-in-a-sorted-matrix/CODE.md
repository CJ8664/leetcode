```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # store the val, row and column of the element that is
        # extracted from the matrix
        h = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(h)
        
        # Pop k times, the last pop would give us the result
        for _ in range(k):
            val, row, col = heapq.heappop(h)
            # If there is still element in the given array, push 
            # the next element
            if col + 1 < len(matrix):
                heapq.heappush(h, (matrix[row][col + 1], row, col + 1))
        return val
            
        
```
