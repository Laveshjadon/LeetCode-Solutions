class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        i = j = 0
        max_cons = 0
        while(j < len(nums)):
            if nums[j] == 1:
            
                max_cons = max(j-i+1,max_cons)
            else:
                i = j + 1
            j += 1
        return max_cons
        