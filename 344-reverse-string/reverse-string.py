class Solution(object):
    def reverseString(self, s):
        def reverse(s,i):
            if i >= len(s)//2:
                return
            s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
            reverse(s,i+1)
        reverse(s,0)

        