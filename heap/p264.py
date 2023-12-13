"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""

import heapq

"""
class Solution:
    def detect_ugly(self, value) -> bool:
        dev_value = [5, 3, 2]
        while dev_value:
            if value % dev_value[0] == 0:
                value /= dev_value[0]
            else:
                dev_value.pop(0)
        return True if value == 1 else False

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            current_index = n - 1
            current_value = 2
            while current_index > 0:
                if self.detect_ugly(current_value):
                    current_index -= 1
                current_value += 1
            return current_value - 1

"""

import heapq


class Solution:
    def __init__(self):
        self.heap = [1]

    def push(self, value):
        self.heap.append(value)
        heapq._siftdown_max(self.heap, 0, len(self.heap) - 1)

    def nthUglyNumber(self, n: int) -> int:
        tmp = n // 3 + 1

        for i in range(tmp):
            for u in [2, 3, 5]:
                self.push(u * (i + 1))

        while len(self.heap) > n + 1:
            heapq._heappop_max(self.heap)

        return self.heap[0]


a = Solution()
print(a.nthUglyNumber(379))
# DONE
