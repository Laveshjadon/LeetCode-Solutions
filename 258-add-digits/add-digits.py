class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            Total = 0 
            for ch in str(num):
                Total += int(ch)
            num = Total
        return num
        