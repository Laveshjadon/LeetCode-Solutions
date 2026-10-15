class Solution(object):
    def maximumSubarraySum(self, nums, k):
        if len(nums) < k:
            return 0
        max_sum = 0
        sums = 0
        freq = {}
        for i in range(k):
            right = nums[i]
            sums += right 
            freq[right] = freq.get(right,0) + 1
        if len(freq) == k:
            max_sum = sums
        for i in range(k,len(nums)):
            left = nums[i - k]
            sums -= left
            
            freq[left] -= 1

            if freq[left] == 0:
                del freq[left]
            right = nums[i]
            sums += right
            freq[right] = freq.get(right, 0) + 1

            if len(freq) == k:
                max_sum = max(sums, max_sum)
        return max_sum


        

       
        