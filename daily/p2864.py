from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_dict = Counter(s)
        if s_dict["1"] == 0:
            return s
        elif s_dict["1"] == 1:
            return "0" * s_dict["0"] + "1"
        else:
            return "1" * (s_dict["1"] - 1) + "0" * s_dict["0"] + "1"


input = "01001010"
a = Solution()
print(a.maximumOddBinaryNumber(input))
