class Solution:
    def compare(self,suc,pre):
        if len(suc)!=len(pre)+1:
            return False
        first=second=0
        while first<len(suc):
            if second<len(pre) and suc[first]==pre[second]:
                first+=1
                second+=1
            else:
                first+=1
        if first==len(suc) and second==len(pre):
            return True
        else:
            return False
        
    def longestStrChain(self, words: List[str]) -> int:
        words=sorted(words,key=len)
        n=len(words)           
        dp=[1]*n
        maxi=1
        for i in range(1,n):
            for prev in range(i): 
                if self.compare(words[i],words[prev]) and dp[prev]+1>dp[i]:
                    dp[i]=dp[prev]+1
            maxi=max(maxi,dp[i])
        return maxi