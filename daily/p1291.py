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
        default_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        low_num, science_low_digits = "{:e}".format(low).split("+")
        _, science_high_digits = "{:e}".format(high).split("+")
        science_low_digits, science_high_digits = int(science_low_digits), int(science_high_digits)
        low_num = int(low_num[0])

        # initial
        result = []
        current_num = low_num
        digits_list = list(range(science_low_digits, science_high_digits + 1))
        while digits_list:
            digits = digits_list.pop(0)
            while current_num + digits <= 9:
                current_result = int("".join(default_num[current_num : current_num + digits + 1]))
                if current_result >= low:
                    if current_result <= high:
                        result.append(current_result)
                    else:
                        return result
                current_num += 1
            current_num = 1
        return result


low, high = 1300, 13000  # 3, 4
a = Solution()
print(a.sequentialDigits(low, high))
