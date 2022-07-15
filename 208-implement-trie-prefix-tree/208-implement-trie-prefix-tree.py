class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        temp = self.trie
        for i, w in enumerate(word):
            if w not in temp or not temp[w]:
                temp[w] = {}
            if i == len(word) - 1:
                temp[w]["#"] = None  
            temp = temp[w]


    def search(self, word: str) -> bool:
        temp = self.trie
        for i, w in enumerate(word):
            if w not in temp:
                return False
            temp = temp[w]
            if i == len(word) - 1:
                return "#" in temp
        return False    
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.trie
        for i, w in enumerate(prefix):
            if w not in temp:
                return False
            temp = temp[w]
            if i == len(prefix) - 1:
                return True
        return False  


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)