class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate rows
        for r in range(len(board)):
            seen = set()
            for c in range(len(board)):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        # Validate cols    
        for c in range(len(board)):
            seen = set()
            for r in range(len(board)):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        # Validate small board
        for rs in range(0, len(board), 3):
            for cs in range(0, len(board), 3):
                seen = set()
                for r in range(len(board) // 3):
                    for c in range(len(board) // 3):
                        if board[r + rs][c + cs] != "." and board[r + rs][c + cs] in seen:
                            return False
                        seen.add(board[r + rs][c + cs])
                
            
        return True
        
        
        