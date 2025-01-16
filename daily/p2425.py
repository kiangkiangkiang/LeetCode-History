from collections import defaultdict
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        index_to_count = defaultdict(int)
        for bit1 in nums1:
            tmp1 = bin(bit1)[2:]
            one_locate1 = [
                len(tmp1) - i - 1 for i in range(len(tmp1)) if tmp1[i] == "1"
            ]
            for i in one_locate1:
                index_to_count[i] += 1 * len(nums2)

        for bit2 in nums2:
            tmp2 = bin(bit2)[2:]
            one_locate2 = [
                len(tmp2) - i - 1 for i in range(len(tmp2)) if tmp2[i] == "1"
            ]

            for i in one_locate2:
                index_to_count[i] += 1 * len(nums1)

        result = 0
        for k, v in index_to_count.items():
            if v % 2 != 0:
                result += 2**k

        return result
        # return 12


nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]

a = Solution()
print(a.xorAllNums(nums1, nums2))
