class Solution(object):
    def rob(self, nums):
        memo = {}
        def solve(n):
            if n <0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = max(solve(n-1),nums[n] + solve(n-2))
            return memo[n]
        return solve(len(nums)-1)
        