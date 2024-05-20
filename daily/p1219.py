from typing import List


class Solution:
    def go(self, start, grid) -> int:
        row_i, col_i = start
        stack = []
        max_amount = -1
        current_memory = set()
        while True:
            # Go Up
            if col_i
            # Go Down
            # Go Left
            # Go Right
        return max_amount

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.memory = set()
        max_amount = -1
        for row_i, row_ele in enumerate(grid):
            for col_i, col_ele in enumerate(row_ele):
                if col_ele != 0 and col_ele not in self.memory:
                    tmp_amount = self.go(start=(row_i, col_i), grid=grid)
                    if tmp_amount > max_amount:
                        max_amount = tmp_amount
        return max_amount


a = Solution()
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(a.getMaximumGold(grid))
