class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = 0
        for task in freq:
            if freq[task] == maxFreq:
                maxCount += 1
        spaces = (maxFreq-1) * max(0, n-maxCount+1)
        maxTasksCount = maxFreq * maxCount
        return max(len(tasks), spaces + maxTasksCount)
        