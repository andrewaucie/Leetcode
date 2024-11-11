class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        
        maxChar, maxCount = max(freq.items(), key=lambda x: x[1])
        if 2 * maxCount - 1 > len(s):
            return ""
        
        res = [''] * len(s)
        index = 0

        while freq[maxChar] > 0:
            res[index] = maxChar
            index += 2
            freq[maxChar] -= 1
        
        for char, count in freq.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                res[index] = char
                index += 2
                count -= 1
        return ''.join(res)