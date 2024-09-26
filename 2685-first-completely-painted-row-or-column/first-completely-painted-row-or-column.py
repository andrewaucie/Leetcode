class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # make sets of rows, cols
        # pop from row, col. if len(set) == 0, return index
        # hashmap to map number to (i,j)
        m = len(mat)
        n = len(mat[0])
        indexMap = {}
        for i in range(m):
            for j in range(n):
                indexMap[mat[i][j]] = (i,j)
        rows = [n] * m
        cols = [m] * n
        for index, num in enumerate(arr):
            i,j = indexMap[num]
            rows[i] -= 1
            cols[j] -= 1
            if rows[i] == 0 or cols[j] == 0:
                return index
        return -1