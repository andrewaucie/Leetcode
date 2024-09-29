class ListNode:
    def __init__(self, freq, prev=None, next=None):
        self.freq = freq
        self.keys = set()
        self.next = next
        self.prev = prev

    # insert curr -> (new)
    def insert(self, new):
        new.next = self.next
        new.next.prev = new
        new.prev = self
        self.next = new
    
    # insert (new) -> curr
    def insertPrev(self, new):
        new.next = self
        self.prev.next = new
        new.prev = self.prev
        self.prev = new

class AllOne:

    def __init__(self):
        self.head = ListNode(freq=0)
        self.tail = ListNode(freq=0, prev=self.head)
        self.head.next = self.tail
        self.keyDict = {}
        self.freqDict = {0: self.head}

    def deleteKeyNode(self, key, freqNode):
        freqNode.keys.remove(key)
        if len(freqNode.keys) == 0:
            del self.freqDict[self.keyDict[key]]
            freqNode.prev.next = freqNode.next
            freqNode.next.prev = freqNode.prev

    def inc(self, key: str) -> None:
        if key not in self.keyDict:
            self.keyDict[key] = 0
        freq = self.keyDict[key] + 1
        oldFreqNode = self.freqDict[self.keyDict[key]]
        # create new freq node and insert
        if freq not in self.freqDict:
            self.freqDict[freq] = ListNode(freq=freq)
            oldFreqNode.insert(self.freqDict[freq])
        if self.keyDict[key] > 0:
            self.deleteKeyNode(key, oldFreqNode)
        self.freqDict[freq].keys.add(key)
        self.keyDict[key] += 1
    
    def dec(self, key: str) -> None:
        freq = self.keyDict[key] - 1
        oldFreqNode = self.freqDict[self.keyDict[key]]
        # create new freq node and insert
        if freq not in self.freqDict:
            self.freqDict[freq] = ListNode(freq=freq)
            oldFreqNode.insertPrev(self.freqDict[freq])
        if self.keyDict[key] > 0:
            self.deleteKeyNode(key, oldFreqNode)
        self.freqDict[freq].keys.add(key)
        self.keyDict[key] -= 1
    
    def getMaxKey(self) -> str:
        for key in self.tail.prev.keys:
            return key
        return ""

    def getMinKey(self) -> str:
        for key in self.head.next.keys:
            return key
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()