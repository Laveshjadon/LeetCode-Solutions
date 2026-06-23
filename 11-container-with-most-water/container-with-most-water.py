class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        result = 0
        while i != j:
            area = 0
            if height[i] >= height[j]:
                area = height[j]*(j-i)
                j -=1
            elif height[i] < height[j]:
                area = height[i] * (j-i)
                i += 1
            result = max(result,area)
        return result