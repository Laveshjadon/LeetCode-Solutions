class Solution(object):
    def twoSum(self, nums, target):
        hashh = {}
        require = 0
        for i in range(len(nums)):
            require = target - nums[i]
            if require in hashh:
                return [hashh[require],i]
            hashh[nums[i]] = i 
        return False
            