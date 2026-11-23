
class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1

            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1

            else:
                curr += 1

        return nums


        