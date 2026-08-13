class Solution(object):
    def isAnagram(self, s, t):
        hashh = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in hashh:
                hashh[ch] += 1
            else:
                hashh[ch] = 1
        for ch in t:
            if ch not in hashh or hashh[ch] == 0:

                return False
            hashh[ch] -= 1
        return True
        