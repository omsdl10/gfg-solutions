class Solution:
    def setBit(self, n):
        # code here
        if n==0:
            return 1
        return n | (n+1)