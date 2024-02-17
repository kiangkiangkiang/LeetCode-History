# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.


# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]


# Constraints:

# 10 <= low <= high <= 10^9


from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        default_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        n = len(str(low))
        possible_result = []

        pass


low, high = 1000, 13000
a = Solution()
print(a.sequentialDigits(low, high))
