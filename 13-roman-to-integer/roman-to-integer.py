class Solution(object):
    def romanToInt(self, s):
    # step 1 write the value of words 
    # define guidline if smaller one  is before the other later than subtract from result else add
    
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
            