from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        
        memo = [-1] * len(jobs)

        def findNextJob(index):
            target_end = jobs[index][1]
            low, high = index + 1, len(jobs)
            while low < high:
                mid = (low + high) // 2
                if jobs[mid][0] >= target_end:
                    high = mid
                else:
                    low = mid + 1
            return low

        def dp(i):
            if i >= len(jobs):
                return 0
            if memo[i] != -1:
                return memo[i]
            skip = dp(i + 1)
            next_job_index = findNextJob(i)
            take = jobs[i][2] + dp(next_job_index)
            memo[i] = max(skip, take)
            return memo[i]
        return dp(0)
