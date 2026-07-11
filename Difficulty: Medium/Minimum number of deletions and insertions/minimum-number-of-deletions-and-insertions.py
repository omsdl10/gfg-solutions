class Solution:
	def minOperations(self, s1, s2):
		m=len(s1)
        n=len(s2)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        lenght=dp[m][n]
        deletion=len(s1)-lenght
        addition=len(s2)-lenght
        return deletion+addition
		