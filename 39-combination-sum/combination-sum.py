class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(path,i,defference):
            if defference == 0:
                result.append(path[:])
                return
            if defference < 0:
                return
            for j in range(i,len(candidates)):
                path.append(candidates[j])

                backtrack(path,j,defference-candidates[j])
                path.pop()
        backtrack([],0,target)
        return result

        