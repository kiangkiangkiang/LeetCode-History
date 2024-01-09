from typing import List


class Solution:
    def pop_stack(self):
        pointer = len(self.stack) - 1
        print(self.stack)
        if len(self.stack[-1]) == 1:
            other_road = self.stack.pop()
        else:
            other_road = [self.stack[-1].pop(0)]
        # print(f"pop num: {len(self.raw_nums) - pointer}")
        # print(f"first add: {other_road}")
        for _ in range(len(self.raw_nums) - pointer):
            self.current.pop()

        self.current += other_road
        tmp = [i for i in self.raw_nums if i not in self.current]
        # print(f"next road num: {tmp}")

        return tmp

    def p(self, nums: List[int]) -> List[List[int]]:
        self.stack = []
        self.current = []
        result = []
        self.raw_nums = nums[:]
        while self.stack or nums:
            # Add
            if len(nums) > 1:
                self.current += [nums.pop(0)]
                self.stack.append(nums[:])
            elif len(nums) == 1:
                self.current += [nums.pop(0)]
            else:
                nums = self.pop_stack()

            if len(self.current) == len(self.raw_nums):
                print(f"current full: {self.current}")
                result.append(self.current[:])
                nums = self.pop_stack()
            if len(result) == 10:
                breakpoint()
            # breakpoint()
        return result


nums = [1, 2, 3, 4]
a = Solution()
print(a.p(nums))
