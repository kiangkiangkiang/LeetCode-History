import heapq
from typing import List

"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. 
On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
"""


class Solution:
    def pk(self):
        while len(self.heap) > 1:
            print(self.heap)
            first = heapq._heappop_max(self.heap)
            second = heapq._heappop_max(self.heap)
            if first - second > 0:
                self.push(first - second)
            else:
                if not self.heap:
                    self.heap = [0]

    def push(self, value):
        self.heap.append(value)
        heapq._siftdown_max(self.heap, 0, len(self.heap) - 1)

    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        heapq._heapify_max(self.heap)
        self.pk()
        print(self.heap)
        return self.heap[0]


input = [10, 3, 8, 9, 4]
a = Solution()
ans = a.lastStoneWeight(input)
print(ans)

# DONE
