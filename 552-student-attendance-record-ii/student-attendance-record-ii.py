class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 1000000007
        def dp(index, absence, late, attendance):
            if late >= 3 or absence >= 2:
                return 0
            if index == n:
                return 1
            if attendance[index][absence][late] != 0:
                return attendance[index][absence][late]
            
            lateCount = dp(index+1, absence, late+1, attendance)
            absenceCount = dp(index+1, absence+1, 0, attendance)
            present = dp(index+1, absence, 0, attendance)

            result = int((lateCount + absenceCount + present) % mod)

            attendance[index][absence][late] = result
            return result
        attendance = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return dp(0, 0, 0, attendance)