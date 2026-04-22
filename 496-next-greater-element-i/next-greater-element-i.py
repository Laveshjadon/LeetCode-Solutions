class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hassh = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                hassh[stack.pop()] = num
            stack.append(num)

        while stack:
            hassh[stack.pop()] = -1
        result = []
        for num in nums1:
            result.append(hassh[num])
        return result 
        

        
        