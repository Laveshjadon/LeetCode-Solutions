class Solution(object):
    def jump(self, nums):
        value = 0
        count = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest,nums[i] + i)


            if i == value:
                count += 1
                value = farthest
        return count 
        