class Solution:
    def leaders(self, arr):
        # code here
        maxelement=arr[-1]
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=maxelement:
                ans.append(arr[i])
                maxelement=arr[i]
        return ans[::-1]
        