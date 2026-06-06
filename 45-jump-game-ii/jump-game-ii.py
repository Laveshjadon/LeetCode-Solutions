class Solution(object):
    def jump(self, nums):
        # keep track of maximum 
        keep_maximum = 0
        # how many moves require it only moves when are index reach to same value to compare
        move = 0
        # it track the value we get by that are we finish the array if not then we took maximum value when index reach to the same value of compare
        compare = 0 
        for i in range(len(nums)-1):
            keep_maximum = max(keep_maximum,nums[i]+i)
            if i == compare:
                move += 1
                compare = keep_maximum
        return move
        