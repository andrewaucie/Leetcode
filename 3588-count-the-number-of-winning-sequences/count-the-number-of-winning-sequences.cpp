class Solution {
public:
    // F-1, W-2.E-3 
    int dp[1004][5][3000];
    const int MOD = 1000000007;
    int f(int index,int prev,int curr,int n,string &a){
        if(index>=n){
            return curr>0;
        }
        if(dp[index][prev+1][curr+1001]!=-1){
            return dp[index][prev+1][curr+1001];
        }
        int count=0;
        if(a[index]=='F'){
            if(prev!=1){
                count = (count + f(index+1,1,curr,n,a))%MOD;
                count%=MOD;
            }
            if(prev!=2){
                count = (count + f(index+1,2,curr+1,n,a))%MOD;
                count%=MOD;
            }
            if(prev!=3){
                count = (count + f(index+1,3,curr-1,n,a))%MOD;
                count%=MOD;
            }
        }
        else if(a[index]=='W'){
            if(prev!=1){
                count = (count + f(index+1,1,curr-1,n,a))%MOD;
                count%=MOD;
            }
            if(prev!=2){
                count  = (count + f(index+1,2,curr,n,a))%MOD;
                count%=MOD;
            }
            if(prev!=3){
                count = (count+ f(index+1,3,curr+1,n,a))%MOD;
                count%=MOD;
            }
        }
        else if(a[index]=='E'){
            if(prev!=1){
                count = (count + f(index+1,1,curr+1,n,a))%MOD;
                count%=MOD;
            }
            if(prev!=2){
                count = (count + f(index+1,2,curr-1,n,a))%MOD;
                count%=MOD;
            }
            if(prev!=3){
                count = (count + f(index+1,3,curr,n,a))%MOD;
                count%=MOD;
            }
        }
        return dp[index][prev+1][curr+1001] = count;
    }
    int countWinningSequences(string s) {
        int n = s.size();
        memset(dp,-1,sizeof(dp));
        return f(0,-1,0,n,s);
    }
};