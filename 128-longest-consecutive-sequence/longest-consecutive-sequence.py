class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sequences = {}
        for n in sorted(list(set(nums))):
            # { n : [left, right, max] }
            sequences[n] = [n, n, 1]
            leftmost, rightmost = n, n
            if n+1 in sequences:
                rightmost = sequences[n+1][1]
                # set n[right] to rightmost
                sequences[n][1] = rightmost
                # set rightmost[left] to n
                sequences[rightmost][0] = n
                # rightmost length + 1
                sequences[n][2] += sequences[rightmost][2]

            if n-1 in sequences:
                leftmost = sequences[n-1][0]
                # set n[left] to leftmost
                sequences[n][0] = leftmost
                # set leftmost[right] to right[n]
                sequences[leftmost][1] = sequences[n][1]
                # leftmost length + 1
                sequences[n][2] += sequences[leftmost][2]
            # update max
            sequences[leftmost][2] = sequences[n][2]
            sequences[rightmost][2] = sequences[n][2]

            longest = max(longest, sequences[n][2])
        return longest
            