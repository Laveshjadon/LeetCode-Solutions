class Solution(object):
    def canConstruct(self, ransomNote, magazine):
    # step 1 we create a hashmap  and add all  magazine
    # step 2 now we compare one by one all ransom value are in hash or not if not getting any of number raise false else true
        hash1 = {} 
        for i in range(len(magazine)):
            if magazine[i] not in hash1:
                hash1[magazine[i]] = 0
            hash1[magazine[i]] += 1
        for i in range(len(ransomNote)):
            if ransomNote[i] not in hash1 or hash1[ransomNote[i]] == 0:
                return False
            
            hash1[ransomNote[i]] -= 1
        return True
