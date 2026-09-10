class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        summ=0
        ans=float('-inf')
        for i in range(len(arr)):
            if summ<0:
                summ=0
            summ+=arr[i]
            ans=max(summ,ans)
        return ans