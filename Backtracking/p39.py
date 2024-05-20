# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current_list = []
        all_possible_candidate = [candidates[:]]
        current_sum = 0
        pointer = 0
        while all_possible_candidate:
            next_possible_candidate = all_possible_candidate[pointer][:]
            if all_possible_candidate[pointer]:
                current_num = all_possible_candidate[pointer].pop(0)
            else:
                all_possible_candidate.pop(pointer)
                pointer -= 1
                if current_list:
                    tmp = current_list.pop()
                    current_sum -= tmp
                continue

            current_sum += current_num
            current_list.append(current_num)

            if current_sum < target:
                all_possible_candidate.append(next_possible_candidate)
                pointer += 1
            elif current_sum == target:
                ans.append(current_list[:])
                tmp = current_list.pop()
                current_sum -= tmp
            else:
                tmp = current_list.pop()
                current_sum -= tmp

        return ans


candidates = [2, 3, 6, 7]
target = 7
a = Solution()
print(a.combinationSum(candidates=candidates, target=target))
print(123)
