class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        numHits = 0
        for i in range(len(self.hits)-1, -1, -1):
            if self.hits[i] > timestamp-300:
                numHits += 1
            else:
                break
        return numHits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)