class Solution(object):
    def twoSum(self, nums, target):
        hashh = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashh:
                return [hashh[value],i]
            else:
                hashh[nums[i]] = i
        
        