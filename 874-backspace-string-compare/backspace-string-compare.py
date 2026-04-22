class Solution(object):
    def backspaceCompare(self, s, t):
        stack1 = []
        for ch in s:
            if ch != "#":
                stack1.append(ch)
            elif len(stack1) != 0:

                stack1.pop()
        stack2 = []
        for ch in t:
            if ch != "#":
                stack2.append(ch)
            elif  len(stack2) != 0:
                stack2.pop()

        return stack1 == stack2       

        