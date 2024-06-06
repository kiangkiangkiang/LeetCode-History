from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # min_list = []
        total = 0
        for start in range(len(arr)):
            last = None
            for end in range(start + 1, len(arr) + 1):
                current = arr[start:end][-1]
                if last:
                    if current < last:
                        # min_list.append(current)
                        total += current
                        last = current
                    else:
                        # min_list.append(last)
                        total += last
                else:
                    # min_list.append(current)
                    total += current
                    last = current
        return total


a = Solution()
arr = [3, 1, 2, 4]
print(a.sumSubarrayMins(arr))
