class Solution:
	def perfectSum(self, arr, target):
		# code here
		dp=[[0 for i in range(target+1)]for j in range(len(arr)+1)]
        dp[0][0]=1
        for i in range(1,len(arr)+1):
            for j in range(target+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(arr)][target]