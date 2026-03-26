class Solution(object):
    def maxArea(self, height):
        p1 = 0 
        p2 = len(height) - 1
        result = 0
        while p1 < p2:
            distance = p2 - p1
            if height[p1] >= height[p2]:
                sums = height[p2] * distance 
                p2 -= 1
            else:
                sums = height[p1] * distance
                p1 += 1
            
            if sums > result:
                result = sums
        return result 
        