class Node:
    __slots__ = ["children", "word"]
    
    def __init__(self):
        self.children = {}
        self.word = False


class Solution:
    def __init__(self):
        self.trie = Node()
        self.dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.max_len = -1
        self.result = set()
    
    def buildTrie(self, words):
        for word in words:
            self.max_len = max(self.max_len, len(word))
            curr = self.trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.word = True
    
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:       
        def dfs(r, c, curr, idx, w):
            while idx < self.max_len:
                if not (0 <= r < len(board)) or not (0 <= c < len(board[0])):
                    return
                if board[r][c] not in curr.children or board[r][c] == "#":
                    return
                
                w += board[r][c]
                curr = curr.children[board[r][c]]
                if curr.word:
                    curr.word = False
                    self.result.add(w)
                
                temp, board[r][c] = board[r][c], "#"
                for nr, nc in self.dir:
                    dfs(r + nr, c + nc, curr, idx + 1, w)
                    
                board[r][c] = temp
                return
        
        self.buildTrie(words)
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, self.trie, 0, "")
        
        return self.result
                