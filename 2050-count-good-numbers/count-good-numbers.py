class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7

        def power(base, exp):
            if exp == 0:
                return 1

            half = power(base, exp // 2)
            result = (half * half) % MOD

            if exp % 2 == 1:
                result = (result * base) % MOD

            return result

        ans = power(20, n // 2)

        if n % 2 == 1:
            ans = (ans * 5) % MOD

        return ans