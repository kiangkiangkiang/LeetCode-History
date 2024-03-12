from typing import List

# The h-index is defined as the maximum value of h such that the given researcher has published
# at least h papers that have each been cited at least h times.


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        max_num = 0
        for i, ele in enumerate(citations):
            accu = i + 1
            if ele >= accu:
                max_num = accu
            else:
                break
        return max_num


citations = [3, 0, 6, 1, 5]
a = Solution()
print(a.hIndex(citations))
