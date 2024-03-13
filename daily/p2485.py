class Solution:
    def pivotInteger(self, n: int) -> int:
        pre_list = []
        post_list = []
        total = 0
        my_list = [i + 1 for i in range(n)]
        for this_int in my_list:
            total += this_int
            pre_list.append(total)

        total = 0
        for this_int in reversed(my_list):
            total += this_int
            post_list.append(total)

        for i, (big, small) in enumerate(zip(pre_list[::-1], post_list)):
            if big < small:
                return -1
            elif big == small:
                return my_list[n - i - 1]


n = 7
a = Solution()
print(a.pivotInteger(n))
