class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        def set_ele(cord, val):
            matrix[cord[0]][cord[1]] = val
        
        def get_ele(cord):
            return matrix[cord[0]][cord[1]]
        
        def swap(top_left, top_right, bottom_right, bottom_left):
            tl = get_ele(top_left)
            tr = get_ele(top_right)
            br = get_ele(bottom_right)
            bl = get_ele(bottom_left)
            
            set_ele(top_left, bl)
            set_ele(top_right, tl)
            set_ele(bottom_right, tr)
            set_ele(bottom_left, br)
        
        for row in range(len(matrix)//2):
            for col in range(row, len(matrix) - 1 - row):
                top_left = (row, col)
                top_right = (col, len(matrix) - 1 - row)
                bottom_right = (len(matrix) - 1 - row, len(matrix) - 1 - col)
                bottom_left = (len(matrix) - 1 - col, row)
                # print(top_left, top_right, bottom_right, bottom_left)
                swap(top_left, top_right, bottom_right, bottom_left)
        