from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        accu_arr = sorted(Counter(arr).items(), key=lambda x: x[1])
        while accu_arr:
            if k >= accu_arr[0][1]:
                k -= accu_arr[0][1]
                accu_arr.pop(0)
            else:
                break
        return len(accu_arr)


k = 1
arr = [1]
a = Solution()

print(a.findLeastNumOfUniqueInts(arr, k))
