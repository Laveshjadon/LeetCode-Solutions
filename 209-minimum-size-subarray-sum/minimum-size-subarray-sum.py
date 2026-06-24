class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0
        sums = 0
        count = float('inf')
        for j in range(len(nums)):
            sums += nums[j]
            while sums >= target:
                count = min(count,j-i+1)
                sums -= nums[i]
                i += 1
        return 0 if count == float('inf') else count