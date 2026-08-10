class Solution(object):
    def canConstruct(self, ransomNote, magazine):
    
        hashh = {}
        for ch in magazine:
            if ch in hashh:
                hashh[ch] += 1
            else:
                hashh[ch] = 1
        for ch in ransomNote:
            if ch not in hashh or hashh[ch] == 0:
                return False
            else:
                hashh[ch] -= 1
        return True