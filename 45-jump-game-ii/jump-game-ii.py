class Solution(object):
    def jump(self, nums):
        jump = 0
        furthest = 0
        one = 0 
        for i in range(len(nums)-1):
            furthest = max(furthest,i+nums[i])
            if i == one:
                jump += 1
                one = furthest
        return jump