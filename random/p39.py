# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
from collections import deque
from typing import List

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.


class Solution:
    def preprocessing(self, candidates, target):
        tmp_result = []
        tmp_candidates = []
        for i in candidates:
            if i == target:
                tmp_result.append([i])
            elif i < target:
                tmp_candidates.append(i)
            else:
                break
        return tmp_candidates, tmp_result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates, result = self.preprocessing(candidates, target)
        raw_candidates = candidates.copy()
        stack = []
        result_memory = set()
        while candidates:
            current_node = candidates.pop()
            candidates_list = [current_node]
            accumulate_sum = current_node
            if other_road_list := [i for i in raw_candidates if i + current_node <= target]:
                stack.append(other_road_list)
            while stack:
                other_road_list = stack.pop()
                other_road = other_road_list.pop()
                if other_road_list:
                    stack.append(other_road_list)

                candidates_list.append(other_road)
                accumulate_sum += other_road

                if accumulate_sum == target:
                    c_list = sorted(candidates_list)
                    c_str = "".join([str(i) for i in c_list])
                    if c_str not in result_memory:
                        result.append(c_list)
                        result_memory.add(c_str)
                else:
                    if other_road_list := [i for i in raw_candidates if i + accumulate_sum <= target]:
                        stack.append(other_road_list)
                    else:
                        candidates_list.pop()
                        accumulate_sum -= other_road

        return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(current_cand, accu, accu_list):
            tmp = []
            for i in current_cand:
                if i + accu == target:
                    result.append(accu_list + [i])
                elif i + accu < target:
                    tmp.append(i)
            return helper(
                tmp,
            )

        helper(candidates, 0, [])


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        raw_candidates = candidates[:]
        result = []
        current_result = []
        dynamic_target = target
        while candidates:
            current = candidates[0]
            print(current_result)
            dynamic_target -= current
            if dynamic_target < 0:
                # last add
                candidates.pop(0)
                dynamic_target += current

                if current_result:
                    dynamic_target += current_result.pop()

                if not candidates and not current_result:
                    current_result = []
                    dynamic_target = 0
                    raw_candidates.pop(0)
                    candidates = raw_candidates[:]
            elif dynamic_target > 0:
                current_result.append(current)
            else:
                result.append(current_result + [current])
                current_result = []
                dynamic_target = 0
                raw_candidates.pop(0)
                candidates = raw_candidates[:]
        return result


candidates = [2, 3, 6, 7]
target = 7
# [[2,2,3],[7]]

a = Solution()
print(a.combinationSum(candidates, target))
