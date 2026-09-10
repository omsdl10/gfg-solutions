class Solution:
    def getSecondLargest(self, arr):
        # code here
        first=-1
        second=-1
        for i in range(len(arr)):
            if arr[i]>first:
                second=first
                first=arr[i]
            elif arr[i]<first and arr[i]>second:
                second=arr[i]
        return second
                