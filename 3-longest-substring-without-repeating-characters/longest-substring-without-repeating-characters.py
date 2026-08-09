class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        result = 0 
        hashh = {}
        for right in range(len(s)):
            curr = s[right]
            if curr in hashh and hashh[curr] >= left:
                left = hashh[curr] + 1
            hashh[curr] = right
            result = max(result,right - left + 1 )
        return result  
        
        