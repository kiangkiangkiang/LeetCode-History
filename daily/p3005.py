import heapq
from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        stat_list = list(Counter(nums).values())
        heapq._heapify_max(stat_list)
        prev = None
        sum = 0
        while stat_list:
            current = heapq._heappop_max(stat_list)
            if prev:
                if prev == current:
                    sum += current
                else:
                    break
            else:
                sum = current
            prev = current
        return sum


s = [1, 2, 3, 3, 4, 4]
a = Solution()
print(a.maxFrequencyElements(s))
