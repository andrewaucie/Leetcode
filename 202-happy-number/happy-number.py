class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSum(n):
            return sum(int(digit)**2 for digit in str(n))
        visited = set()
        while n != 1:
            digitSum = sum(int(digit)**2 for digit in str(n))
            if digitSum in visited:
                return False
            visited.add(digitSum)
            n = digitSum
        return True
