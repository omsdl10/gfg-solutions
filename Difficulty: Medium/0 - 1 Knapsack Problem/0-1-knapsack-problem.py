class Solution:
    def knapsack(self, W, val, wt):
        # code here
        dp=[[0 for i in range(W+1)]for j in range(len(wt)+1)]
        for i in range(1,len(wt)+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(wt)][W]