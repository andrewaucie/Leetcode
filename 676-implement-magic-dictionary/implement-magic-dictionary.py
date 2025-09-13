class MagicDictionary:

    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            trie = self.trie
            for w in word:
                if w not in trie:
                    trie[w] = {}
                trie = trie[w]
            trie['*'] = True

    def search(self, searchWord: str) -> bool:
        trie = self.trie
        for i in range(len(searchWord)):
            for ch in trie:
                if ch == '*' or ch == searchWord[i]:
                    continue
                matched = True
                currTrie = trie[ch]
                for j in range(i+1, len(searchWord)):
                    if searchWord[j] not in currTrie:
                        matched = False
                        break
                    currTrie = currTrie[searchWord[j]]
                if matched and '*' in currTrie:
                    return True
            if searchWord[i] not in trie:
                return False
            trie = trie[searchWord[i]]
        return False
    
    

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)