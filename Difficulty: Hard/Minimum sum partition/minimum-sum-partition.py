# class Solution:
# 	def minDifference(self, arr):
# 		# code here
# 		total=sum(arr)
# 		dp=[[False for i in range(total+1)] for j in range(len(arr)+1)]
# 		for i in range(len(arr)+1):
# 		    dp[i][0]=True
# 		for i in range(1,len(arr)+1):
# 		    for j in range(1,total+1):
# 		        if arr[i-1]<=j:
# 		            dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
# 		        else:
# 		            dp[i][j]=dp[i-1][j]
# 		minimum=float('inf')
# 		for i in range(total//2+1):
# 		    if dp[len(arr)][i]:
# 		        minimum=min(minimum,abs(total-2*i))
# 		return minimum
class Solution:
    def minDifference(self, arr):
        total=sum(arr)
        dp=[False]*(total+1)
        dp[0]=True
        for num in arr:
            for j in range(total, num - 1, -1):
                dp[j]=dp[j] or dp[j-num]
        ans = float('inf')
        for s in range(total//2+1):
            if dp[s]:
                ans=min(ans,total-2*s)
        return ans		    