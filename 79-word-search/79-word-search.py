class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_row = len(board)
        num_col = len(board[0])
        word_len = len(word)
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        # optimization 1: If word is greater than board
        if word_len > num_row * num_col:
            return False
        
        # optimization 2: If board has all chars of word
        c = collections.Counter()
        w = collections.Counter(word)
        for row in board:
            c.update(row)
        for ch in w:
            if ch not in c or w[ch] > c[ch]: return False
            
        def search(r, c, i):
            if i == len(word): return True
            if not (0 <= r < num_row) or not(0 <= c < num_col): return False
            if board[r][c] != word[i] or board[r][c] == "#": return False
        
            temp, board[r][c] = board[r][c], "#"
            result = any([search(r + nr, c + nc, i + 1) for nr, nc in dir])
            if not result:
                board[r][c] = temp
            return result
        
        # Now run expensive DFS
        for r in range(num_row):
            for c in range(num_col):
                if search(r, c, 0):
                    return True
        return False
                
                
        