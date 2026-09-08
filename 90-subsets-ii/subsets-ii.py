class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        def backtrack(path,i):
            
            result.append(path[:])
                 
            for j in range(i,len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                backtrack(path,j+1)
                path.pop()
        backtrack([],0)
        return result

        