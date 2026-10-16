class Solution(object):
    def minSubArrayLen(self, target, nums):
        result = float('inf')
        sums = 0
        left = 0
        right = 0
        while right < (len(nums)):
            sums += nums[right]
            while sums >= target:
                result = min(result,right-left+1)
                sums -= nums[left]
                left += 1
            
            right += 1
        return 0 if result == float('inf') else result

            

        