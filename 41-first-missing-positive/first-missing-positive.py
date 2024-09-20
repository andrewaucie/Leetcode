class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = 1
        visited = set()
        for n in nums:
            if n > 0:
                visited.add(n)
                while k in visited: 
                    k += 1
        return k