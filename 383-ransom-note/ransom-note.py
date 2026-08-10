class Solution(object):
    def canConstruct(self, ransomNote, magazine):
    
        hashh = {}
        
        for a in magazine:
            if a in hashh:
                hashh[a] += 1
            else:
                hashh[a] = 1
        for b in ransomNote:
            if b not in hashh or hashh[b] == 0:
                return False
            else:
                hashh[b] -= 1
        return True