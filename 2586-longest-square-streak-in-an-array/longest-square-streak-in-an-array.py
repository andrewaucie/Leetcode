class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longest = 1
        numMap = {}
        for n in set(nums):
            numMap[n] = [n,n,1]
            if n**2 in numMap:
                # n marks start of this streak
                numMap[n][1] = numMap[n**2][1]  # update end on curr num
                numMap[n][2] += numMap[n**2][2] # update size
                numMap[numMap[n**2][0]] = numMap[n]
                numMap[numMap[n**2][1]] = numMap[n]

            if n**0.5 in numMap:
                # n marks end of this streak
                numMap[n][0] = numMap[n**0.5][0]  # update start on curr num
                numMap[n][2] += numMap[n**0.5][2] # update size
                numMap[numMap[n**0.5][0]] = numMap[n]
                numMap[numMap[n**0.5][1]] = numMap[n]

            longest = max(longest, numMap[n][2])
        return longest if longest != 1 else -1

        # [2,4,16,256,...]
        # [3,9,81,6561,..]
        # [5,25,625,..]
        # [6,36,..]
        # [8,64,..]
        # input = [4,3,6,16,8,2]

        # [3,9,81,6561]
        # {n: [start, end, size]}
        # {4,3,6,16}
        # {3: [3,3,1], 6: [6,6,1], 16: [2,16,3], 2:[2,16,3], 4:[2,16,3], 256}

        # union find approach to connect streaks, get max size streak at the end (or maintain max size throughout)