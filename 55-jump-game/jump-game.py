class Solution(object):
    def canJump(self, nums):
        remaining = 0
        for i in range(len(nums)):
            if i > remaining:
                return False
            remaining = max(remaining,i + nums[i]) 
            if remaining >= len(nums) - 1:
                return True
        return True 


