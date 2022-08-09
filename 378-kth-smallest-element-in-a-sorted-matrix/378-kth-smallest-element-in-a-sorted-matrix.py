class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(h)
        
        for _ in range(k):
            val, row, col = heapq.heappop(h)
            if col + 1 < len(matrix):
                heapq.heappush(h, (matrix[row][col + 1], row, col + 1))
        return val
            
        