class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(path,i,defference):
            if defference == 0:
                result.append(path[:])
                return
            if i >= len(candidates) or defference < 0:
                return
            
            path.append(candidates[i])
            backtrack(path,i,defference-candidates[i])
            path.pop()
            backtrack(path,i+1,defference)

        backtrack([],0,target)
        return result


        