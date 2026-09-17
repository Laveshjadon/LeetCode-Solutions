class Solution(object):
    def climbStairs(self, n):
        memo = {}
        def solve(num):
            if num == 0:
                return 1
            if num < 0:
                return 0
            if num in memo:
                return memo[num]
            memo[num] = solve(num-1) + solve(num-2)
            
            return memo[num]
        return solve(n)
            
        