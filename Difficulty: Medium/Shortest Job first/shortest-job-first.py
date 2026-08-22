class Solution:
    def solve(self, bt):
        # code here
        summ=0
        wt=0
        bt.sort()
        for i in range(len(bt)-1):
            wt+=summ
            summ+=bt[i]
        wt+=summ
        return wt//len(bt)
        