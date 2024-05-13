# 861. Score After Flipping Matrix
# Medium
# Topics
# Companies
# You are given an m x n binary matrix grid.

# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score after making any number of moves (including zero moves).

# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

from typing import List


class Solution:
    def sum_as_binary(self, grid) -> int:
        total = 0
        for l in grid:
            for i, ele in enumerate(reversed(l)):
                if ele == 1:
                    total += 2**i
        return total

    # def hor_check(self, grid):
    #     tmp_max = -1
    #     tmp_index = -1
    #     for row, l in enumerate(grid):
    #         zero_total = 0
    #         one_total = 0
    #         for i, ele in enumerate(reversed(l)):
    #             if ele == 1:
    #                 one_total += 2**i
    #             else:
    #                 zero_total += 2**i

    #         if zero_total > one_total and zero_total > tmp_max:
    #             tmp_max = zero_total
    #             tmp_index = row

    #     return tmp_index, tmp_max

    def hor_check(self, grid):
        tmp_max = -1
        tmp_index = -1
        for row in range(len(grid)):
            zero_total = 0
            one_total = 0
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    one_total += 2 ** (len(grid[0]) - col - 1)
                else:
                    zero_total += 2 ** (len(grid[0]) - col - 1)

            if zero_total > one_total and zero_total > tmp_max:
                tmp_max = zero_total
                tmp_index = row

        return tmp_index, tmp_max

    def ver_check(self, grid):
        tmp_max = -1
        tmp_index = -1
        for col in range(len(grid[0])):
            zero_total = 0
            one_total = 0
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    one_total += 2 ** (len(grid[0]) - col - 1)
                else:
                    zero_total += 2 ** (len(grid[0]) - col - 1)

            if zero_total > one_total and zero_total > tmp_max:
                tmp_max = zero_total
                tmp_index = col

        return tmp_index, tmp_max

    def rotate_hor(self, grid, index_h):
        zero = 0
        one = 0
        for i, ele in enumerate(grid[index_h]):
            if ele == 1:
                one += 2 ** (len(grid[index_h]) - i - 1)
                grid[index_h][i] = 0
            else:
                zero += 2 ** (len(grid[index_h]) - i - 1)
                grid[index_h][i] = 1
        return grid, zero - one

    def rotate_ver(self, grid, index_v):
        zero = 0
        one = 0
        for i in range(len(grid)):
            if grid[i][index_v] == 1:
                one += 2 ** (len(grid[0]) - index_v - 1)
                grid[i][index_v] = 0
            else:
                zero += 2 ** (len(grid[0]) - index_v - 1)
                grid[i][index_v] = 1
        return grid, zero - one

    def matrixScore(self, grid: List[List[int]]) -> int:
        index_v, index_h = None, None
        current_sum = self.sum_as_binary(grid)
        while index_h != -1 or index_v != -1:
            index_h, num_h = self.hor_check(grid)
            index_v, num_v = self.ver_check(grid)

            if index_h == -1 and index_v == -1:
                break

            if num_h > num_v:
                grid, gap_sum = self.rotate_hor(grid, index_h)
            else:
                grid, gap_sum = self.rotate_ver(grid, index_v)

            current_sum += gap_sum
        return current_sum


a = Solution()
grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
# grid = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]
print(a.matrixScore(grid))
