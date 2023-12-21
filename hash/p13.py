"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000









"""


class Solution:
    reduce_dict = {
        "I": 1,
        "X": 10,
        "C": 100,
    }
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def add(self, s):
        sum = 0
        for c in reversed(s):
            if c in self.reduce_dict:
                sum -= self.roman_to_int[c]
            else:
                sum += self.roman_to_int[c]
        return sum

    def romanToInt(self, s: str) -> int:
        split_index = s.find("I")
        left_s = s[:split_index]
        right_s = s[split_index:]
        right_sum = self.add(right_s[1:]) - 1 if right_s[-1] != "I" else len(right_s)
        return right_sum + self.add(left_s)


input = "MCMXCIV"
a = Solution()
ans = a.romanToInt(input)
print(ans)
