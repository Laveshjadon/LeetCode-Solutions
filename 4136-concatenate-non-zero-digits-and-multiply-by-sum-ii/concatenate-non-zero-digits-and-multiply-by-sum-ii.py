from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        pos = []
        digits = []

        # Store positions and values of non-zero digits
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        # Powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix sum of digits
        prefSum = [0] * (n + 1)
        for i in range(n):
            prefSum[i + 1] = prefSum[i] + digits[i]

        # Prefix concatenated value
        prefVal = [0] * (n + 1)
        for i in range(n):
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            digitSum = prefSum[right + 1] - prefSum[left]

            x = (
                prefVal[right + 1]
                - prefVal[left] * pow10[length]
            ) % MOD

            ans.append((x * digitSum) % MOD)

        return ans