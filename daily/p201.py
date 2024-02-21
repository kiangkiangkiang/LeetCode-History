# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.


# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0


# class Solution:
#     def __init__(self):
#         self.mapping_tbl = [2**i for i in reversed(range(32))]
#         self.index = list(reversed(range(32)))

#     def num_to_digits(self, num) -> set:
#         if num == 0:
#             return {}
#         elif num == 1:
#             return {0}
#         else:
#             result = []
#             if num % 2 != 0:
#                 result.append(0)
#             for i, two_times in zip(self.index, self.mapping_tbl):
#                 if two_times <= num:
#                     result.append(i)
#                     num -= two_times

#                 if num <= 1:
#                     break
#             return set(result)

#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         current_intersection = set(range(32))  # which has 1
#         for num in range(left, right + 1):
#             one_locate = self.num_to_digits(num)
#             # current_intersection = current_intersection.intersection(one_locate)
#             # print(num)
#             # print(current_intersection)
#             if not current_intersection:
#                 return 0
#         breakpoint()

#         result = 0
#         for i in current_intersection:
#             result += 2**i
#         return result


class Solution:
    def __init__(self):
        self.mapping_tbl = [2**i for i in reversed(range(32))]
        self.index = list(reversed(range(32)))

    def find_largeest_two_times(self, num):
        for i, two_times in zip(self.index, self.mapping_tbl):
            if two_times <= num:
                return i, two_times

    def sum_result(self, result):
        s = 0
        for i in result:
            s += 2**i
        return s

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = []

        while left > 0 and right > 0:
            left_digits, left_decimals = self.find_largeest_two_times(left)
            right_digits, right_decimals = self.find_largeest_two_times(right)
            if left_digits != right_digits:
                break
            else:
                result.append(left_digits)
                left -= left_decimals
                right -= right_decimals
        return self.sum_result(result)


left = 600000000
right = 2147483645

left = 4
right = 7
a = Solution()
print(a.rangeBitwiseAnd(left, right))
