class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return False
            if idx > len(word) or board[r][c] != word[idx] or board[r][c] == "#":
                return False
            
            temp, board[r][c] = board[r][c], "#"
            for nr, nc in dirs:
                if dfs(r + nr, c + nc, idx + 1):
                    board[r][c] = temp
                    return True
            board[r][c] = temp
            return False
                
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
        
        