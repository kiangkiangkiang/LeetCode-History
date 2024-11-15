from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        quantities.sort(reverse=True)
        result_list = [-1 for _ in quantities]
        worker_list = [1 for _ in quantities]
        max_num = None
        while True:
            for i in range(len(quantities)):
                if result_list[i] == -1:
                    worker_list[i] += 1
                else:
                    pass

                n -= 1
                result_list[i] = int(quantities[i] / worker_list[i])

                if n <= 0:
                    print(result_list)
                    return max(result_list)
            current += 1


n = 22
quantities = [25, 11, 29, 6, 24, 4, 29, 18, 6, 13, 25, 30]
# [30, 29, 29, 25, 25, 24, 18, 13, 11, 6, 6, 4]
a = Solution()
print(a.minimizedMaximum(n, quantities))
