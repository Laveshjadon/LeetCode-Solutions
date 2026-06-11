class Solution(object):
    def productExceptSelf(self, nums):
        left = 1
        right = 1
        result = [1]*len(nums)
        # in this we are multiplying starting to end ex [1,2,3,4] become [1,2,6,24]
        for i in range(len(nums)):
            result[i] = left
            left *= nums[i]
        # now it was doing same this with reverse [1,2,3,4] become [24,12,4,1] 
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i]*right # already exist values multiplying by right side values 
            right *= nums[i]
        
        return result
        
    # 