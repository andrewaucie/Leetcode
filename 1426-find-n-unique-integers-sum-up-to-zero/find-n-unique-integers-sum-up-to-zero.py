class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n):
            arr.append(i)
        arr.append(- n * (n-1) // 2)
        return arr