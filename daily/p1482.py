import bisect
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        bloomDay = sorted([(ele, i) for i, ele in enumerate(bloomDay)], key=lambda x: x[0])
        current_bloom = []
        while bloomDay:
            while True:
                b_day, arr_idx = bloomDay.pop(0)
                bisect.insort(current_bloom, arr_idx)
                if not bloomDay or bloomDay[0][0] != arr_idx:
                    break

            last = None
            counter = 0
            counter_m = 0
            for b in current_bloom:
                if last != None and last + 1 == b:
                    counter += 1
                else:
                    counter = 1

                last = b

                if counter == k:
                    counter_m += 1
                    counter = 0
                    last = None

                if counter_m == m:
                    return b_day

        return -1


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1

bloomDay = [30, 49, 11, 66, 54, 22, 2, 57, 35]
m = 3
k = 3
a = Solution()
print(a.minDays(bloomDay=bloomDay, m=m, k=k))
