class Solution(object):
    def letterCombinations(self, digits):
        hashmap ={2 : 'abc',3 : 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7 : 'pqrs', 8:'tuv', 9: 'wxyz' }
        result = []
        def Backtrack(path,index):
            if len(path) == len(digits):
                result.append("".join(path))
                return 
            pair = hashmap[int(digits[index])]
            for char in pair:
                path.append(char)
                Backtrack(path,index + 1)
                path.pop()

            if not digits:
                return []
        Backtrack([],0)
        return result 
