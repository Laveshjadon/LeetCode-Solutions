class Solution(object):
    def combinationSum(self, candidates, target):

        res = []
        def backtrack(start_index, current_path, remaining_target):
            if remaining_target == 0:
                res.append(list(current_path))
                return
            if remaining_target < 0:
                return 
            for i in range(start_index,len(candidates)):
                current_path.append(candidates[i])


                backtrack(i,current_path, remaining_target - candidates[i])

                current_path.pop()

        backtrack(0,[],target)
        return res


        