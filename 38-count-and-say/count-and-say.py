class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        RLE = "1"
        while n > 1:
            newRLE = ""
            prev, count = 0, 1
            for i in range(1, len(RLE)):
                if RLE[i] == RLE[prev]:
                    count += 1
                else:
                    newRLE += str(count) + RLE[prev]
                    prev, count = i, 1
            newRLE += str(count) + RLE[prev]
            RLE = str(newRLE)
            n -= 1
        return RLE