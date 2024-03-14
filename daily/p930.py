# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.


# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1] # 1, 1, 2, 2, 3
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0 # 0, 0, 0, 0, 0
# Output: 15

from typing import List


class Solution:
    def __init__(self):
        self.zero_combination_map = {}

    def counter_zero_combination(self, n):
        if n not in self.zero_combination_map:
            counter = 2
            for i in range(n):
                this_int = i + 1
                if this_int == 1:
                    accumu = 1
                else:
                    accumu += counter
                    counter += 1
            self.zero_combination_map[n] = accumu
            return accumu
        else:
            return self.zero_combination_map[n]

    def check_prefix_postfix(self, sparse_nums, outer_i, inner_i):
        n = len(sparse_nums) - 1
        outer_sum = 0
        inner_sum = 0
        if outer_i == 0:
            outer_sum += sparse_nums[outer_i][0]
        else:
            outer_sum += sparse_nums[outer_i][0] - sparse_nums[outer_i - 1][0] - 1

        if inner_i == n:
            inner_sum += len(self.nums) - 1 - sparse_nums[inner_i][0]
        else:
            inner_sum += sparse_nums[inner_i + 1][0] - sparse_nums[inner_i][0] - 1

        if outer_sum == 0:
            return inner_sum
        elif inner_sum == 0:
            return outer_sum
        else:
            return inner_sum * outer_sum + inner_sum + outer_sum

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            result = []
            tmp_result = 0
            for i, n in enumerate(nums):
                if n == 0:
                    tmp_result += 1
                else:
                    if tmp_result > 0:
                        result.append(tmp_result)
                        tmp_result = 0
            if tmp_result > 0:
                result.append(tmp_result)

            final_total = 0
            for i in result:
                final_total += self.counter_zero_combination(n=i)
            return final_total
        else:
            if not (sparse_nums := [[i, n] for i, n in enumerate(nums) if n != 0]):
                return 0

            final_total = 0
            self.nums = nums
            for outer_i in range(len(sparse_nums) - 1):
                if sparse_nums[outer_i][1] == goal:
                    final_total += 1
                    final_total += self.check_prefix_postfix(sparse_nums, outer_i=outer_i, inner_i=outer_i)
                    continue
                accumu = sparse_nums[outer_i][1]
                for inner_i in range(outer_i + 1, len(sparse_nums)):
                    accumu += sparse_nums[inner_i][1]
                    if accumu == goal:
                        final_total += 1
                        final_total += self.check_prefix_postfix(sparse_nums, outer_i=outer_i, inner_i=inner_i)
                        break
            if sparse_nums[-1][1] == goal:
                final_total += 1
                final_total += self.check_prefix_postfix(
                    sparse_nums, outer_i=len(sparse_nums) - 1, inner_i=len(sparse_nums) - 1
                )

            return final_total


class Solution:
    def __init__(self):
        self.zero_combination_map = {}

    def counter_zero_combination(self, n):
        if n not in self.zero_combination_map:
            counter = 2
            for i in range(n):
                this_int = i + 1
                if this_int == 1:
                    accumu = 1
                else:
                    accumu += counter
                    counter += 1
            self.zero_combination_map[n] = accumu
            return accumu
        else:
            return self.zero_combination_map[n]

    def get_all_zero_comination(self, nums):
        result = []
        tmp_result = 0
        for i, n in enumerate(nums):
            if n == 0:
                tmp_result += 1
            else:
                if tmp_result > 0:
                    result.append(tmp_result)
                    tmp_result = 0
        if tmp_result > 0:
            result.append(tmp_result)

        final_total = 0
        for i in result:
            final_total += self.counter_zero_combination(n=i)
        return final_total

    def get_windows(self, n, total_len):
        if n > total_len:
            return []
        else:
            result = []
            for i in range(total_len):
                if i + n - 1 > total_len - 1:
                    break
                else:
                    result.append([i, i + n - 1])
            return result

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        one_location = [i for i, n in enumerate(nums) if n != 0]
        if goal == 0:
            return self.get_all_zero_comination(nums)

        if not one_location:
            return 0

        if not (all_windows := self.get_windows(goal, len(one_location))):
            return 0
        else:
            result = 0
            for i, window in enumerate(all_windows):
                result += 1
                pre = 0
                post = 0
                if i == 0:
                    # start
                    pre = one_location[window[0]]
                else:
                    pre = one_location[window[0]] - one_location[all_windows[i - 1][0]] - 1

                if i == len(all_windows) - 1:
                    # last
                    post = len(nums) - one_location[window[1]] - 1
                else:
                    post = one_location[all_windows[i + 1][1]] - one_location[window[1]] - 1

                if pre == 0:
                    result += post
                elif post == 0:
                    result += pre
                else:
                    result += pre * post + pre + post
            return result


nums = [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
goal = 5
# 10
a = Solution()
print(a.numSubarraysWithSum(nums=nums, goal=goal))
