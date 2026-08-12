class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 0 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                value = n % 10 
                total += value * value
                n = n // 10
            n = total 
        return n == 1

            

        