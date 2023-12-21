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

    def romanToInt(self, s: str) -> int:
        prev_c = ""
        sum = 0
        for c in s[::-1]:
            if prev_c != "" and self.roman_to_int[prev_c] > self.roman_to_int[c] and c in self.reduce_dict:
                sum -= self.roman_to_int[c]
            else:
                sum += self.roman_to_int[c]
            prev_c = c
        return sum


input = "III"
a = Solution()
ans = a.romanToInt(input)
print(ans)
