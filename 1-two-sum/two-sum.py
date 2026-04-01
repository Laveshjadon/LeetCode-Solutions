class Solution(object):
    def twoSum (self,arr, target):
        seen ={}
        for i, num in enumerate(arr):
            need = target - num

            if need in seen:
                return [seen[need],i]
            seen[num] = i
        