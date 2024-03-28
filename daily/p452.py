# There are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points where
# points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend.
# You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
# bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def get_points_neightbor(self, points):
        # return: {group: [neighbor, sum of neighbor]}
        result = {}
        check_num = len(points)
        new_points = sorted(points, key=lambda x: x[0]) * 2
        for group, ele in enumerate(new_points):
            if group == check_num:
                break
            result[group] = [[], 0]  # initial
            for neighbor_group in range(group + 1, group + check_num):
                if (
                    ele[0] <= new_points[neighbor_group][0] <= ele[1]
                    or ele[0] <= new_points[neighbor_group][1] <= ele[1]
                ):
                    result[group][0].append(neighbor_group % check_num)
                    result[group][1] += 1
        return result

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_neighbor = self.get_points_neightbor(points)
        points_neighbor = sorted(points_neighbor.items(), key=lambda x: x[1][1])  # sorted by sum
        exist_group = set([i for i in range(len(points))])
        arr_num = 0
        for group, neighbor_info in points_neighbor:
            if group not in exist_group:
                continue

            exist_group.remove(group)  # drop itself
            arr_num += 1
            for drop_group in neighbor_info[0]:
                if drop_group in exist_group:
                    exist_group.remove(drop_group)

            if not exist_group:
                break
        return arr_num


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pass


inp = [[1, 2], [2, 3], [3, 4], [4, 5]]
inp = [[1, 2], [3, 4], [5, 6], [7, 8]]
inp = [[10, 16], [2, 8], [1, 6], [7, 12]]
inp = [[2, 3], [2, 3]]
inp = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]  # 2
inp = [[1, 9], [7, 16], [2, 5], [7, 12], [9, 11], [2, 10], [9, 16], [3, 9], [1, 3]]  # 2
a = Solution()
print(a.findMinArrowShots(inp))
