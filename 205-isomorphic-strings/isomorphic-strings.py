class Solution(object):
    def isIsomorphic(self, s, t):
        hassh_s = {}
        hassh_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]
            
            if ch_s not in hassh_s:
                hassh_s[ch_s] = ch_t
            else:
                if hassh_s[ch_s] != ch_t:
                    return False

            if ch_t not in hassh_t:
                hassh_t[ch_t] = ch_s
            else:
                if hassh_t[ch_t] != ch_s:
                    return False

        return True

