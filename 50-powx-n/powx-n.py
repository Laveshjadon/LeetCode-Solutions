class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
            
        half = self.myPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

        