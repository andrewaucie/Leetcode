class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # [2,4,16,256,...]
        # [3,9,81,6561,..]
        # [5,25,625,..]
        # [6,36,..]
        # [8,64,..]
        # input = [4,3,6,16,8,2]
        longest = 1
        numMap = {}
        for n in set(nums):
            numMap[n] = [n,n,1]
            if n**2 in numMap:
                # n marks start of this streak
                numMap[n**2][0] = n  # update start on next num
                numMap[n][1] = numMap[n**2][1]  # update end on curr num
                numMap[n][2] += numMap[n**2][2] # update size

            if math.sqrt(n) in numMap:
                # n marks end of this streak
                numMap[math.sqrt(n)][1] = n  # update end on prev num
                numMap[n][0] = numMap[math.sqrt(n)][0]  # update start on curr num
                numMap[n][2] += numMap[math.sqrt(n)][2] # update size

            for adj in (math.sqrt(n), n**2):
                if adj in numMap:
                    print(numMap[adj])
                    numMap[numMap[adj][0]] = numMap[n]
                    numMap[numMap[adj][1]] = numMap[n]
            longest = max(longest, numMap[n][2])
        return longest if longest != 1 else -1

        # [3,9,81,6561]
        # {n: [start, end, size]}
        # {4,3,6,16}
        # {3: [3,3,1], 6: [6,6,1], 16: [2,16,3], 2:[2,16,3], 4:[2,16,3], 256}

        # union find approach to connect streaks, get max size streak at the end (or maintain max size throughout)