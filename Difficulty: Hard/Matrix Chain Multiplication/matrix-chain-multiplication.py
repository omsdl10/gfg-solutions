def MCM(arr,i,j,dp):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    temp=float('inf')
    for k in range(i,j):
        tempans=MCM(arr,i,k,dp)+MCM(arr,k+1,j,dp)+arr[i-1]*arr[k]*arr[j]
        temp=min(temp,tempans)
    dp[i][j]=temp
    return temp
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        dp=[[-1]*101 for i in range(101)]
        return MCM(arr,1,len(arr)-1,dp)
        