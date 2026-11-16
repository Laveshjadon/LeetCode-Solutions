class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            new_str = ""
            for i in range(0,len(s),k):
                group = s[i:i+k]
                group_sum = 0
                for ch in group:
                    group_sum += int(ch)
                new_str += str(group_sum)
            s = new_str
        return s
        