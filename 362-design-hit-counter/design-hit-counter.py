class HitCounter:

    def __init__(self):
        self.timestamps = []
        self.l = 0
        from bisect import bisect_left

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.l += 1
        
    def getHits(self, timestamp: int) -> int:
        left = 0
        right = self.l-1
        target = timestamp - 300
        while left <= right:
            m = (left + right) // 2
            if self.timestamps[m] <= target:
                left = m + 1
            else:
                right = m - 1

        return self.l - left        
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)