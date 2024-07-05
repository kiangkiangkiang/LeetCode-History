import bisect
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        real_candidate = []
        epoch = 0
        while epoch + k <= len(bloomDay):
            start = epoch
            while start + k <= len(bloomDay):
                real_candidate.append(max(bloomDay[start : start + k][:]))
                start = start + k
                # if len(candidate) == m:
                #     real_candidate.append(max(candidate))
                #     break
            epoch += 1
            while epoch % k == 0 and epoch + k <= len(bloomDay):
                epoch += 1
        if len(real_candidate) < m:
            return -1
        else:
            real_candidate.sort()
            return real_candidate[m - 1]


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1

bloomDay = [30, 49, 11, 66, 54, 22, 2, 57, 35]
m = 3
k = 2
a = Solution()
print(a.minDays(bloomDay=bloomDay, m=m, k=k))
