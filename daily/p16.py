from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        other_road = []
        current_list = []
        current_road = nums.copy()
        n = len(nums)
        pointer = 0
        pointer_list = []
        sum_list = []
        while current_road or other_road:
            if len(current_list) < 3:
                current = nums[pointer]
                pointer += 1
                other_road.append(nums[pointer : n - 3 + pointer])
                current_list.append(current)
                pointer_list.append(pointer)
            else:
                sum_list.append(sum(current_list))
                while other_road:
                    current_list.pop()
                    pointer = pointer_list.pop()
                    current_road = other_road.pop()
                    if current_road:
                        break

        print(123)
        return 1


nums = [-1, 2, 1, -4]
target = 1
a = Solution()
print(a.threeSumClosest(nums, target))
