class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            heapq.heappush(self.maxHeap, -num)
            return

        if len(self.maxHeap) == len(self.minHeap):
            if num >= -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        elif len(self.maxHeap) > len(self.minHeap):
            if num >= -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                movedElement = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, movedElement)
                heapq.heappush(self.maxHeap, -num)
        else:
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                movedElement = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -movedElement)
                heapq.heappush(self.minHeap, num)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()