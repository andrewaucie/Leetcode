class UnionFind: # structure to find and represent disjunct sets/classes
    def __init__(self):
        self.classes = {} # mapping from element to its class representative
    
    def find(self, x): # find representative for x. If x has no representative, make it its own representative
        if x not in self.classes:
            self.classes[x] = x
        return self.classes[x]
    
    def union(self, x, y): # group two classes/sets
        px, py = self.find(x), self.find(y)
        if px == py:
            return 
        if px > py: # smaller representative shall represent both elements
            px, py = py, px # swap 
        for c, r in self.classes.items():
            if r == py:
                self.classes[c] = px # set new representative
            
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:  
        uf = UnionFind()
        for s0, s1 in synonyms:
            uf.union(s0,s1) # update class memberships, consider transitivity
        words = text.split(' ')
        res = [] 
        def bt(i, sequence): # backtracking method
            if i == len(words):
                res.append(' '.join(sequence)) # reached end of sentence, so append current sequence to results
                return 
            r = uf.find(words[i]) # will add words[i] to union find, no matter if synonyme or not
            for s in sorted([x for x in uf.classes.keys() if uf.find(x) == r]): # find all synonyms 
                bt(i+1, sequence + [s]) # start backtracking at next word
        bt(0, [])
        return res