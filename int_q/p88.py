from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1, pointer2 = 0, 0

        while pointer2 < n or pointer1 < m + n - 1:
            if nums1[pointer1] == 0:
                nums1.insert(pointer1, nums2[pointer2])
                pointer2 += 1
            else:
                if nums2[pointer2] <= nums1[pointer1]:
                    nums1.insert(pointer1, nums2[pointer2])
                    pointer2 += 1
                else:
                    pointer1 += 1

        for i in reversed(range(len(nums1))):
            if i <= m + n - 1:
                break
            else:
                nums1.pop(i)


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
