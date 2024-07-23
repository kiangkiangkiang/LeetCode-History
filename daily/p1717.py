# 1717. Maximum Score From Removing Substrings
# Medium
# Topics
# Companies
# Hint
# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.


# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20


class Solution:
    def do_detemine(self, s, first, second):
        result = 0
        last = None
        while True:
            while (num := s.count(first[0])) != 0:
                s = s.replace(first[0], "")
                result = result + (first[1] * num)

            while (num := s.count(second[0])) != 0:
                s = s.replace(second[0], "")
                result = result + (second[1] * num)

            if last == result:
                break
            else:
                last = result
        return result

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            return self.do_detemine(s, first=["ab", x], second=["ba", y])
        else:
            return self.do_detemine(s, first=["ba", y], second=["ab", x])


s = "cdbcbbaaabab"
x = 4
y = 5
# expect: 19

s = "aabbaaxybbaabb"
x = 5
y = 4
# expect: 20
a = Solution()
print(a.maximumGain(s, x, y))
