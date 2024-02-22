# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

from collections import deque

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
from typing import List


class Solution:
    def find_two_times(self, num):
        if num == 0:
            return 0
        elif num == 1:
            return 0
        else:
            counter = 0
            while num > 1:
                num = num >> 1
                counter += 1
            return counter

    def num_to_bit(self, num) -> list:
        result = None
        while num > 0:
            two_times = self.find_two_times(num)
            if not result:
                result = [0] * (two_times + 1)

            result[two_times] = 1
            num -= 2**two_times

        return result if result else [0]

    def countBits(self, n: int) -> List[int]:
        return [sum(self.num_to_bit(i)) for i in range(n + 1)]


n = 5
a = Solution()
print(a.countBits(n))
