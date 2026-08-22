class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def backtrack(path,start,end):
            if len(path) == n * 2:
                result.append(path[:])
                return
            if start < n:
                backtrack(path + "(",start + 1,end)
            if end < start:
                backtrack(path + ")",start, end + 1)
        backtrack("",0,0)
        return result
