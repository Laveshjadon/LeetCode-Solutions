class Solution(object):
    def checkValidString(self, s):
        high = 0
        low = 0 
        for i in s:
            if i == '(':
                high += 1
                low += 1
            elif i == ')':
                high -= 1
                low -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(low,0)
        return low == 0