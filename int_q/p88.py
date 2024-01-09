from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(len(nums1) - m):
            nums1.pop()

        if nums2:
            nums1.extend(nums2)

        nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

a = Solution()
a.merge(nums1, m, nums2, n)
print(nums1)
