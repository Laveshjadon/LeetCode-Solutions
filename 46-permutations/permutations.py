class Solution(object):
    def permute(self, nums):
        
        result = []
        def check(path):
            if path == len(nums):
                result.append(nums[:])
                
            for i in range(path,len(nums)):
                nums[i] , nums[path] = nums[path],nums[i]
                check(path+1)
                nums[i] , nums[path] = nums[path],nums[i]
        check(0)
        return result

        