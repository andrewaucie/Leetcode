class RandomizedSet:

    def __init__(self):
        self.numMap = {}   # { val: index }
        self.indexMap = {} # { index: val }
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.n += 1
        self.numMap[val] = self.n
        self.indexMap[self.n] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False

        # get topmost element (val=top, index=self.n)
        topVal = self.indexMap[self.n]

        # save val's index
        index = self.numMap[val]

        # delete val's mapping
        del self.numMap[val]
        del self.indexMap[index]

        # check if we're not deleting top
        if index < self.n:
            # move topmost element into index
            self.indexMap[index] = topVal
            self.numMap[topVal] = index
        self.n -= 1
        return True

    def getRandom(self) -> int:
        index = random.randint(1, self.n)
        return self.indexMap[index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()