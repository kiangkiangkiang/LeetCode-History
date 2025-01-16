from typing import List


class Solution:
    def is_non_decrease(self, arr):
        last = None
        for num in arr:
            if last is None or num >= last:
                last = num
            else:
                return False
        return True

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if self.is_non_decrease(arr):
            return 0

        for total in range(1, len(arr) - 1):
            for sub_start in range(len(arr) - total + 1):
                sub_arr = arr[:sub_start] + arr[sub_start + total :]
                if self.is_non_decrease(sub_arr):
                    return len(arr) - len(sub_arr)

        return len(arr) - 1


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        pass

    
    

arr = [1, 2, 8, 9, 3, 10, 4, 2, 3, 5]
# arr = [1,3,5,6,0,5,7,8,9]
arr = [2, 2, 2, 1, 1, 1]
a = Solution()
print(a.findLengthOfShortestSubarray(arr))
