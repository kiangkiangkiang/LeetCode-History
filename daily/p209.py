# 209. Minimum Size Subarray Sum
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_arr = []
        tmp = 0
        for num in [0] + nums:
            tmp += num
            sum_arr.append(tmp)

        status_tmp = []
        left_pointer = 0
        right_pointer = len(sum_arr) - 1
        candidate = 0
        min_ans = 1000000
        while left_pointer < right_pointer:
            if sum_arr[right_pointer] - sum_arr[left_pointer] >= target:
                candidate = right_pointer - left_pointer
                if candidate < min_ans:
                    min_ans = candidate
            else:
                if status_tmp:
                    left_pointer, right_pointer = status_tmp.pop()
                    continue
                else:
                    break

            if left_pointer + 1 < right_pointer:
                status_tmp.append((left_pointer, right_pointer - 1))
                left_pointer += 1
            else:
                break

        return min_ans if min_ans != 1000000 else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]

# target = 6
# nums = [10, 2, 3]

# target = 4
# nums = [1, 4, 4]
a = Solution()
print(a.minSubArrayLen(target=target, nums=nums))
