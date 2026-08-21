class Solution(object):
    def permute(self, nums):
        result = []
        def backtracking(path,used):
            if len(path) == len(nums):
                result.append(path[:])
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(path,used)

                path.pop()
                used[i] = False
        backtracking([],[False]*len(nums))
        return result

            

        