class Solution(object):
    def subsets(self, nums):
        result = []
        def backtrack(path,index):
            if len(nums) == index:
                result.append(path[:])
                return
            path.append(nums[index])
            backtrack(path,index+1)
            path.pop()
            backtrack(path,index+1)
        backtrack([],0)
        return result

        