from typing import List
from collections import defaultdict


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        
        for event in events:
            pass


events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
a = Solution()
print(a.maxTwoEvents(events))
