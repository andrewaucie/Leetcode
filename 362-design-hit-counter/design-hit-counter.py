class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        numHits = 0
        for i in range(len(self.hits)-1, -1, -1):
            if self.hits[i][0] > timestamp-300:
                numHits += self.hits[i][1]
            else:
                break
        return numHits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)