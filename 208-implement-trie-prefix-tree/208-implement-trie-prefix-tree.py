class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        current_dict = self.trie 
        for char in word:
            if char not in current_dict:
                current_dict[char] = {}
            current_dict = current_dict[char]
        current_dict['_'] = '_'


    def search(self, word: str) -> bool:
        current_dict = self.trie
        for char in word:
            if char in current_dict:
                current_dict = current_dict[char]
            else:
                return False
        return '_' in current_dict  
        

    def startsWith(self, prefix: str) -> bool:
        current_dict = self.trie
        for char in prefix:
            if char in current_dict:
                current_dict = current_dict[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)