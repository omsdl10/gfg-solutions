class Solution:
    def longestConsecutive(self, arr):
        # code here
        arr.sort()
        count=1
        ans=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                continue
            if arr[i]==arr[i-1]+1:
                count+=1
            else:
                count=1
            ans=max(count,ans)
        return ans