"""
class Solution:
    def numDecodings(self, s: str) -> int:
        total_sol = 1
        zero_skip = False
        for i in reversed(range(len(s))[1:]):
            if zero_skip:
                zero_skip = False
                continue
            if s[i] == "0":
                if int(s[i - 1]) > 2:
                    return 0
                else:
                    zero_skip = True
            else:
                if s[i - 1] != "0" and int(s[i - 1] + s[i]) <= 26:
                    total_sol = total_sol * 2
        return total_sol
"""

""" time limit
class Solution:
    def numDecodings(self, s: str) -> int:
        def do_find(s, index):
            if index == 0 and s[index] == "0":
                return "non-exist"

            if index <= 0:
                self.num_of_ans += 1
            else:
                if s[index] == "0":
                    if int(s[index - 1]) > 2 or int(s[index - 1]) == 0:
                        return "non-exist"
                    else:
                        do_find(s, index - 2)
                else:
                    do_find(s, index - 1)

                    if s[index - 1] != "0" and int(s[index - 1] + s[index]) <= 26:
                        do_find(s, index - 2)

        self.num_of_ans = 0

        result = do_find(s, index=len(s) - 1)

        return self.num_of_ans if result != "non-exist" else 0
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        total = 1
        s = list(s)
        n = len(s) - 1
        zero_fix = "0" not in s
        while s:
            current = s.pop(-1)
            if s:
                if current == "0" and (int(s[-1]) > 2 or int(s[-1]) <= 0):
                    return 0

                if s[-1] == "0":
                    s.pop(-1)
                    if s and int(s[-1]) < 3:
                        s.pop(-1)
                    else:
                        return 0
                else:
                    if int(s[-1] + current) <= 26:
                        total *= 2
                        s.pop(-1)
            else:
                if current == "0":
                    return 0
        return total + 1 if zero_fix and n >= 2 else total


class Solution:
    def numDecodings(self, s: str) -> int:
        total = 1
        s = list(s)
        n = len(s) - 1
        zero_fix = "0" not in s
        last_value_is_zero = False
        prev_value = ""
        while s:
            current = s.pop(-1)
            if prev_value == "0":
                if current == "0" or int(current) > 3:
                    return 0
                continue
            else:
                if current == "0":
                    continue
                else:
                    total *= 2
            prev_value = current
            if s:
                s.pop(-1)

        if last_value_is_zero:
            return 0
        else:
            return total


class Solution:
    def normal_process(self, s: str) -> int:
        n = len(s)
        tmp = 1
        breakpoint()
        if s == "":
            return 1
        else:
            for i in range(n)[::2]:
                if i + 1 < n and int(s[i] + s[i + 1]) <= 26:
                    tmp *= 2
        return tmp + 1 if n > 2 else tmp

    def numDecodings(self, s: str) -> int:
        zero_split = s.split("0")
        last_str = zero_split.pop(-1)

        total = 0
        if zero_split:
            for each_s in zero_split:
                if each_s == "":
                    return 0
                else:
                    if int(each_s[-1]) > 2:
                        return 0
                    total += self.normal_process(s=each_s[:-1])
        return total * self.normal_process(last_str) if total != 0 else self.normal_process(last_str)


input = "1223"
# input = "11106"
# input = "27"
# input = "2101"
input = "111"
# input = "12"
# input = "06"
# input = "106"
# input = "11503"
# input = "00"
# input = "27"
# input = "10"
input = "123123"
a = Solution()
print(a.numDecodings(input))
