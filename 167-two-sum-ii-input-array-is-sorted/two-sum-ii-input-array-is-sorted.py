class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i != j:
            count = numbers[i] + numbers[j]

            if count < target:
                i += 1
            elif count > target:
                j -= 1
            else:
                return [i+1,j+1]
