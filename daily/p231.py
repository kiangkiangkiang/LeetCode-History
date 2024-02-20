class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a = 1
        while a <= n:
            if a == n:
                return True
            a = a << 1
        return False


n = 2**31 + 1


a = Solution()
print(a.isPowerOfTwo(n))
