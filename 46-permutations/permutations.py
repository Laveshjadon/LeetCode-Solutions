class Solution(object):
    def permute(self, nums):
        result = []
        def backtracking(path):
            if path == len(nums):
                result.append(nums[:])
            for i in range(path, len(nums)):
                nums[i],nums[path] = nums[path],nums[i]
                backtracking(path+1)
                nums[i],nums[path] = nums[path],nums[i]
        backtracking(0)
        return result

        