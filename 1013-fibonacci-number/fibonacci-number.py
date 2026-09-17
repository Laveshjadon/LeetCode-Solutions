class Solution(object):
    def fib(self, n):
        def solve(num):
            if num <= 1:
                return num
            return solve(num - 1) + solve(num - 2)
        return solve(n)
         
        