class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, left = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r == 0:
                        top = True
                    if c == 0:
                        left = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
               
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if top:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if left:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                    
            
        