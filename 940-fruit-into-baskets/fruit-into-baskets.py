class Solution(object):
    def totalFruit(self, fruits):
        maps ={}
        left = 0
        right = 0
        result = 0
        while right < len(fruits):
            maps[fruits[right]] = maps.get(fruits[right],0) + 1
            while len(maps) > 2:
                maps[fruits[left]] -= 1
                if maps[fruits[left]] == 0:
                    del maps[fruits[left]]
                left += 1
            result = max(result,right - left + 1)
            right += 1
        return result 
            
        
        