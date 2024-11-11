class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        
        maxChar, maxCount = max(freq.items(), key=lambda x: x[1])
        if 2 * maxCount - 1 > len(s):
            return ""
        
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        string = ""
        prev_count, prev_char = 0, ''
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            string += char
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            prev_count, prev_char = count + 1, char
        return string