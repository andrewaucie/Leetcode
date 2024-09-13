class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
             prefix[i] = prefix[i - 1] ^ arr[i - 1]
             
        result = []
    
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])
    
        return result