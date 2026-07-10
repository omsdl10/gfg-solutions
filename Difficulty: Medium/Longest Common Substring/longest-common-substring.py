class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        m=len(s1)
        n=len(s2)
        dp=[[0]*(n+1) for i in range(m+1)]
        ans=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    ans=max(dp[i][j],ans)
                else:
                    dp[i][j]=0
        return ans