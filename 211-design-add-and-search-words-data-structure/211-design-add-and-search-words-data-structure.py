class Node:
    __slots__ = ["children", "word"]
    
    def __init__(self):
        self.children = {}
        self.word = False
    def __repr__(self):
        return str(self.word) + ": " + str(self.children)

class WordDictionary:

    def __init__(self):
        self.trie = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True


    def search(self, word: str) -> bool:
        def dfs(curr, idx):
            while idx < len(word):
                if word[idx] == ".":
                    for child in curr.children.values():
                        if dfs(child, idx + 1):
                            return True
                if word[idx] not in curr.children:
                    return False
                curr = curr.children[word[idx]]
                idx += 1
            return curr.word
        return dfs(self.trie, 0)
            
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)