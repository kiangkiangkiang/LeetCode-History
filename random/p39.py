from typing import List

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        new_candidates = candidates.copy()
        iter_candidates = candidates.copy()
        sum_candidates = candidates.copy()

        while new_candidates:
            this_int = new_candidates.pop()
            tmp = []
            for i in iter_candidates:
                if i + this_int < target:
                    iter_candidates.append()


candidates = [2, 3, 6, 7]
# [[2,2,3],[7]]
target = 7
a = Solution()
print(a.combinationSum(candidates, target))
