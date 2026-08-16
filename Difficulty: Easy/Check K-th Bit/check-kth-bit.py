class Solution:
    def checkKthBit(self, n, k):
        # code here
        if n & 1<<k :
            return True 
        return False