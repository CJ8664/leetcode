class TrieNode:
    __slots__ = ["children", "is_word"]
    def __init__(self):
        self.children = {}
        self.is_word = False
        
    def __repr__(self):
        return f"{self.children}:{self.is_word}"

class Solution:
    def __init__(self):
        self.trie = TrieNode()
        self.max_word_len = -1
        self.board = None
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
    def buildTrie(self, words: List[str]):
        for word in words:
            curr = self.trie
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_word = True
            self.max_word_len = max(self.max_word_len, len(word))
        
    def search(self, r, c, trie, word):
        if not (0 <= r < self.num_r) or not (0 <= c < self.num_c): return
        if self.board[r][c] not in trie.children or self.board[r][c] == "#": return
        # print(word, r, c, self.board)        
        trie = trie.children[self.board[r][c]]
        word += self.board[r][c]
        if trie.is_word: self.result.add(word)
        
        temp, self.board[r][c] = self.board[r][c], "#"
        for nr, nc in self.dir:
            self.search(r + nr, c + nc, trie, word)
        self.board[r][c] = temp
                    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_r, self.num_c = len(board), len(board[0])
        self.board = board
        self.buildTrie(words)
        self.result = set()
        for r in range(self.num_r):
            for c in range(self.num_c):
                self.search(r, c, self.trie, "")
        return self.result   