class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original):
            return []
        res = []
        idx = 0
        for i in range(m):
            row = []
            for i in range(idx, idx+n):
                row.append(original[i])
            res.append(row)
            idx += n
        return res