class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        def backtrack(path,remaining, index):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return 
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(path,remaining - candidates[i],i+1)
                path.pop()
        backtrack([],target,0)
        return result


        