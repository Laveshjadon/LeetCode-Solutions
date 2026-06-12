class Solution(object):
    def romanToInt(self, s):
    # step 1 write the meanig of words 
    # define guidline if I is before the other later it whould be latter value that comes after smaller one(that's not I ) - value of hash
    # if value comes after that we can add directly in the values 
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        output = 0
        for i in range(1,len(s)):
            if roman[s[i-1]] < roman[s[i]]:
                output -= roman[s[i-1]] 
            else:
                output += roman[s[i-1]] 
        output = output + roman[s[len(s)-1]]
        return output 
        
            