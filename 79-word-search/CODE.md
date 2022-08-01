```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ROWS, COLS, WORD_LEN = len(board), len(board[0]), len(word)
        
        # optimization 1: If word is greater than board
        if WORD_LEN > ROWS * COLS:
            return False
        
        # optimization 2: If board has all chars of word
        c = collections.Counter()
        w = collections.Counter(word)
        for row in board:
            c.update(row)
        for ch in w:
            if ch not in c or w[ch] > c[ch]: return False
        
        def dfs(r, c, idx):
            if idx == WORD_LEN: return True
            if not (0 <= r < ROWS) or not (0 <= c < COLS): return False
            if board[r][c] != word[idx] or board[r][c] == "#": return False
            
            temp, board[r][c] = board[r][c], "#"
            for nr, nc in dirs:
                if dfs(r + nr, c + nc, idx + 1):
                    return True
            board[r][c] = temp
            return False
        
        # Now run expensive DFS
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
        
        
```
