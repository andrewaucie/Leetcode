class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result, nums, visited, curr_result
        result = []

        def dfs(result, curr_result, visited):
            if len(curr_result) == len(nums):
                result.append(curr_result.copy())
                return
            
            for item in nums:
                if item not in visited:
                    curr_result.append(item)
                    visited.add(item)
                    dfs(result, curr_result, visited)
                    visited.remove(item)
                    curr_result.pop()

        dfs(result, [], set())
        return result
        
