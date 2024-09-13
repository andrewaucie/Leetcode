class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0] * len(arr)
        xors[0] = arr[0]
        for i in range(1, len(arr)):
            xors[i] = xors[i-1] ^ arr[i]
        res = []
        for l, r in queries:
            if l == 0:
                res.append(xors[r])
            else:
                res.append(xors[l-1] ^ xors[r])
        return res