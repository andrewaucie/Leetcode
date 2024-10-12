class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['*'] = ''
    
    def search(self, word: str) -> bool:
        return self.searchDot(word, self.root)
    
    def searchDot(self, word, cur):
        for i in range(len(word)):
            if word[i] == '.':
                for nextLetter in cur:
                    if self.searchDot(word[i+1:], cur[nextLetter]):
                        return True
                return False
            elif word[i] not in cur:
                return False
            cur = cur[word[i]]
        return '*' in cur


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)