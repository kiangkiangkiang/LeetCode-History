from typing import List


class Solution:
    def get_permutations(self, nums):
        per_list = []
        for n in nums:
            tmp = []
            for p in per_list:
                tmp.append([n] + p)
            per_list.extend(tmp)
            per_list.append([n])
        return per_list

    def get_bin(self, num):
        initial_bin = [0, 0, 0, 0, 0]
        if num - 16 >= 0:
            initial_bin[0] += 1
            num -= 16
        if num - 8 >= 0:
            initial_bin[1] += 1
            num -= 8
        if num - 4 >= 0:
            initial_bin[2] += 1
            num -= 4
        if num - 2 >= 0:
            initial_bin[3] += 1
            num -= 2
        if num - 1 >= 0:
            initial_bin[4] += 1
            num -= 1
        return initial_bin

    def get_xor(self, a, b):
        result = [0, 0, 0, 0, 0]
        pointer = 0
        while pointer < 5:
            if (a[pointer] == 1 and b[pointer] != 1) or (a[pointer] != 1 and b[pointer] == 1):
                result[pointer] = 1
            pointer += 1
        return result

    def get_num(self, bin):
        initial_bin = 0
        for i, ele in enumerate(bin):
            if ele == 1:
                initial_bin += 2 ** (5 - i - 1)
        return initial_bin

    def subsetXORSum(self, nums: List[int]) -> int:
        perimutations_list = self.get_permutations(nums)
        current_xor_result = None
        total = 0
        for subset in perimutations_list:
            current_xor_result = None
            for each_nums in subset:
                if current_xor_result:
                    current_xor_result = self.get_xor(current_xor_result, self.get_bin(each_nums))
                else:
                    current_xor_result = self.get_bin(each_nums)
            total += self.get_num(current_xor_result)

        return total


# nums = [5, 1, 6]
nums = [3, 4, 5, 6, 7, 8]
a = Solution()
print(a.subsetXORSum(nums=nums))
