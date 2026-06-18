class Solution(object):
    def twoSum (self,arr, target):
        # step 1 we add the arr values in the dict and we map them with index
        # step 3 now we find which number we need if it was in hash than we return both index 
        # step 3 if not than just map value with number
        hashh = {}
        for i in range(len(arr)):
            need = target - arr[i]
            if need in hashh:
                return [hashh[need],i]
            hashh[arr[i]] = i
        return []
        