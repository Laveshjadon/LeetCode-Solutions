class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        ans = 0

        while(left<=right):
            mid = left + (right - left)//2
            if target > nums[mid]:
                ans = mid + 1
                left = mid + 1
            else:
                right = mid -1
        return ans