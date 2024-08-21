class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # return the number of unique pairs
        answ=0
        # create a dictionary: d[x]==nums.count(x)
        d={}
        for x in nums:
            if x in d: d[x]+=1
            else:      d[x]=1
        
        if k: # k>0
            answ=sum(x+k in d for x in d.keys())
        else: # k==0
            answ=sum(k>1 for k in d.values())
                
        return answ