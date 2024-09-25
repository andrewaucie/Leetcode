class HitCounter:

    def __init__(self):
        self.hitCount = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hitCount[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        hits = 0
        for time in self.hitCount:
            if time > timestamp - 300:
                hits += self.hitCount[time]
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)