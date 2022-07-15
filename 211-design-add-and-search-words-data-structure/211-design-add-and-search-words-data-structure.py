class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        temp = self.trie
        for ch in word:
            if ch not in temp:
                temp[ch] = {}
            temp = temp[ch]
        temp["#"] = 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # print word, self.trie
        temp = self.trie
        def helper(word, temp):
            
            for idx, ch in enumerate(word):
                if ch == '.':
                    res = []
                    for x, t in temp.items():
                        if x == "#":
                            res.append(False)
                        else:
                            res.append(helper(word[idx+1:], t))
                    return any(res)
                if ch not in temp:
                    return False
                else:
                    temp = temp[ch]
            if "#" in temp:
                return True
            else:
                return False
        return helper(word, temp)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)