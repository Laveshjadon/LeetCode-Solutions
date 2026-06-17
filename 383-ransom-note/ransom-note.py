class Solution(object):
    def canConstruct(self, ransomNote, magazine):
    # step 1 we create a hashmap  and add all  magazine
    # step 2 now we compare one by one all ransom value are in hash or not if not getting any of number raise false else true
        hash1 = {} 
        for ch in magazine:
            hash1[ch] = hash1.get(ch,0) + 1
        
        for ch in ransomNote:
            if ch not in hash1 or hash1[ch] == 0:
                return False
            hash1[ch] -= 1
        return True