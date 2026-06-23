class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                triplet = [nums[i],nums[j],nums[k]]
                sums = nums[i] + nums[j] + nums[k]
                if sums < 0:
                    j += 1
                elif sums > 0:
                    k -= 1
                else:
                    
                    result.append(triplet)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                
        return result 
        