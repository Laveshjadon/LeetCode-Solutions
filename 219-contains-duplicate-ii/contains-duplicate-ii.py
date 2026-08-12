class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashh = {}
        for i in range(len(nums)):
            if nums[i] in hashh and  abs(hashh[nums[i]]-i) <= k:
                return True
            else:
                hashh[nums[i]] = i
        return False

                

        
        