class Solution(object):
    def nextPermutation(self, nums):
        index = -1 
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] > nums[i]:
                index = i
                break

        if index == -1:
            return nums.reverse()
        
        for i in range(len(nums)-1,index,-1):
            if nums[i] > nums[index]:
                nums[index],nums[i] = nums[i],nums[index]
                break
        nums[index+1:] = reversed(nums[index+1:])
        return nums
