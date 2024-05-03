from typing import List


class Solution:
    def get_one_locate(self, grid) -> list:
        result = []
        for i, r in enumerate(grid):
            for u, c in enumerate(r):
                if c == "1":
                    result.append([i, u])
        return result

    def numIslands(self, grid: List[List[str]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        one_locate = self.get_one_locate(grid)

        if not one_locate:
            return 0

        current = one_locate.pop(0)
        counter = 1
        stack = []
        while one_locate:
            # down
            if [current[0] + 1, current[1]] in one_locate:
                stack.append([current[0] + 1, current[1]])

            # left
            if [current[0], current[1] - 1] in one_locate and [current[0], current[1] - 1] not in stack:
                stack.append([current[0], current[1] - 1])

            # right
            if [current[0], current[1] + 1] in one_locate:
                current = [current[0], current[1] + 1]
                one_locate.remove(current)
            else:
                if stack:
                    current = stack.pop()
                    one_locate.remove(current)
                else:
                    current = one_locate.pop(0)
                    counter += 1
        return counter


a = Solution()
# grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
# grid = [["0"]]
# grid = [["1"]]
# grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]  # expect 1

grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
print(a.numIslands(grid))
