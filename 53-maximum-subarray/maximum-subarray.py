class Solution(object):
    def maxSubArray(self, nums):
        curr = nums[0]
        maxx = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < curr + nums[i]:
                curr = curr + nums[i]
            else:
                curr = nums[i]

            if curr > maxx:
                maxx = curr
        return maxx
        