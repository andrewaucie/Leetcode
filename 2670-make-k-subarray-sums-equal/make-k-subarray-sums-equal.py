class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # check how many need to equal
        # i == (i+k)%n
        n = len(arr)
       
        ans = 0
        visited = [False]*n

        for i in range(n):
            if not visited[i]:
            # Collect elements in the current group
                group = []
                
                while not visited[i]:
                    group.append(arr[i])
                    visited[i] = True
                    i = (i+k)%n
            # Sort the group
                group.sort()
            # Find the median
                median = group[len(group) // 2]
            # Calculate the cost to make all elements in the group equal to the median
                ans += sum(abs(x - median) for x in group)
        
        return ans