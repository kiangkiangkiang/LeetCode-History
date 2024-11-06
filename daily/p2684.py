from typing import List


class Solution:
    def move(self, current_index, row_bound, col_bound):
        result = []
        if current_index[1] + 1 < col_bound:
            if current_index[0] - 1 >= 0:
                result = [
                    [current_index[0] - 1, current_index[1] + 1],
                    [current_index[0], current_index[1] + 1],
                ]
            else:
                result = [
                    [current_index[0], current_index[1] + 1],
                ]

            if current_index[0] + 1 < row_bound:
                result.append([current_index[0] + 1, current_index[1] + 1])
        return result

    def maxMoves(self, grid: List[List[int]]) -> int:
        next_step = [[i, 0] for i in range(len(grid))]
        next_step_stack = []
        current_list = []
        result = 0
        count = 0
        while next_step or next_step_stack:
            current_index = next_step.pop()
            current_num = grid[current_index[0]][current_index[1]]
            if current_list == [] or current_list[-1] < current_num:
                current_list.append(current_num)
                count += 1
                next_step_stack.append(next_step[:])
                next_step = self.move(current_index, len(grid), len(grid[0]))

            if not next_step:
                # print(current_list)
                if current_list:
                    if count - 1 > result:
                        result = count - 1
                        if result == len(grid[0]) - 1:
                            break
                    while next_step_stack:
                        next_step = next_step_stack.pop()
                        current_list.pop()
                        count -= 1
                        if next_step:
                            break

        return result


grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]

a = Solution()
print(a.maxMoves(grid))
