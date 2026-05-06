class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and num[stack[-1]] > num[i]:
                
                stack.pop()
                k -= 1
            stack.append(i)
        while k > 0:
            stack.pop()
            k -= 1
        result = ''.join(num[i] for i in stack).lstrip('0')
        return result if result else "0"

        