class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        flag=0
        if x < 0:
            flag = 1
            x = abs(x)
        while(x>0):
            r = x%10
            n = n*10+r
            x = x//10
        if n > pow(2,31)-1 or n < -pow(2,31):
            return 0
        if flag:
            return -1*n
        else:
            return n