class Solution(object):
    def isIsomorphic(self, s, t):
        hashh_s = {}
        hashh_t = {}
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            curr_s = s[i]
            curr_t = t[i]
            if curr_s in hashh_s and hashh_s[curr_s] != curr_t:
                return False
            hashh_s[curr_s] = curr_t
            if curr_t in hashh_t and hashh_t[curr_t] != curr_s:
                return False
            hashh_t[curr_t] = curr_s
        return True
            