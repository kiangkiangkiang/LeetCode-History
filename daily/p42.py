# Given n non-negative integers representing an elevation map
# where the width of each bar is 1,
# compute how much water it can trap after raining.


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] # 1 + 1 + 2 + 1 + 1
# Output: 6
# Explanation: The above elevation map (black section)
# is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
# 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Input: height = [4,2,0,3,2,5] # 2 + 4 + 1 + 2
# Output: 9

from collections import Counter, defaultdict
from typing import List


class Solution:
    def pop_start_zero(self, height):
        while height:
            if height[0] == 0:
                height.pop(0)
            else:
                break
        return height

    def check_calculate(self, height):
        height_stat = Counter(height)
        height_stat_list = sorted(height_stat.items(), key=lambda x: x[0])
        height_stat = dict(height_stat_list)
        index_mapping = {key: i for i, key in enumerate(height_stat.keys())}
        result = []

        for h in height:
            height_stat[h] -= 1
            if height_stat[h] > 0:
                result.append(True)
                continue
            else:
                if index_mapping[height_stat[h]] + 1 >= len(height_stat_list) - 1:
                    result.append(False)
                    continue
                else:
                    for i in range(index_mapping[height_stat[h]] + 1, len(height_stat_list)):
                        if height_stat_list[i]:
                            pass

    def trap(self, height: List[int]) -> int:
        height = self.pop_start_zero(height)
        can_calculate = self.check_calculate(height)

        if not height:
            return 0


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
a = Solution()
print(a.trap(height=height))
