# You are given an array of positive integers nums of length n.

# A polygon is a closed plane figure that has at least 3 sides.
# The longest side of a polygon is smaller than the sum of its other sides.

# Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak
# where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak,
# then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

# The perimeter of a polygon is the sum of lengths of its sides.

# Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.


# Example 1:

# Input: nums = [5,5,5]
# Output: 15
# Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        equal_reset = 0
        current_ploygon, new_nums = nums[:3], nums[3:]
        current_sum = sum(current_ploygon)
        if current_ploygon[0] + current_ploygon[1] <= current_ploygon[2]:
            if new_nums:
                equal_reset += current_sum
            else:
                return -1

        while new_nums:
            current_side = new_nums.pop(0)
            if current_side > current_sum:
                equal_reset += current_side
                current_sum += current_side
            elif current_side == current_sum:
                equal_reset += current_sum
                current_sum += current_side
            else:
                equal_reset = 0
                current_sum += current_side

        return current_sum - equal_reset if current_sum - equal_reset > 0 else -1


# nums = [1, 12, 1, 2, 5, 50, 3]
# nums = [5, 5, 5]
# nums = [1, 1, 2, 4]
# nums = [1, 5, 1, 5]
nums = [1, 33, 25, 42, 12, 2, 20, 14, 4, 22]
a = Solution()
print(a.largestPerimeter(nums))
