class Solution:
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    res = []
    indexMap = defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            indexMap[i+j].append(mat[i][j])
    for index, val in indexMap.items():
        if index % 2 == 0:
            res.extend(val[::-1])
        else:
            res.extend(val)
    return res