class Solution:

    def swap(self, a, b):
        #code here
        a=a^b
        b=a^b
        a=a^b
        print(a, b)
