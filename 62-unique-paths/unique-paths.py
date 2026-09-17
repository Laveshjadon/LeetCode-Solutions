class Solution(object):
    def uniquePaths(self, m, n):
        memo = {}
        def solve(c,r):
            if r == 0 or c ==0:
                return 0
            if r == 1 and c == 1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = solve(c-1,r) + solve(c,r-1)
            return memo[(r,c)]
        return solve(m,n)
        
                

        