from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        memory = set()
        current_list = []
        candidates.sort()
        all_possible_candidate = [candidates[:]]
        current_sum = 0
        pointer = 0
        while all_possible_candidate:
            if all_possible_candidate[pointer]:
                current_num = all_possible_candidate[pointer].pop(0)
                next_possible_candidate = all_possible_candidate[pointer][:]
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
                str_list = "".join([str(i) for i in current_list])
                if str_list not in memory:
                    memory.add(str_list)
                    ans.append(current_list[:])

                tmp = current_list.pop()
                current_sum -= tmp
            else:
                tmp = current_list.pop()
                current_sum -= tmp

        return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
a = Solution()
print(a.combinationSum(candidates, target))
