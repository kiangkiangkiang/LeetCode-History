# 1750. Minimum Length of String After Deleting Similar Ends
# Medium
# Topics
# Companies
# Hint
# Given a string s consisting only of characters 'a', 'b', and 'c'.
# You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).


# Example 1:

# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.
# Example 2:

# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".
# Example 3:

# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".


class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        current_len = len(s)
        while len(s) >= 2 and s[0] == s[-1]:
            control_char = s[0]
            head_cont_pop = True
            tail_cont_pop = True
            while head_cont_pop or tail_cont_pop:
                if head_cont_pop:
                    s.pop(0)

                if tail_cont_pop:
                    s.pop(-1)

                if len(s) >= 2:
                    head_cont_pop = s[0] == control_char
                    tail_cont_pop = s[-1] == control_char
                elif len(s) == 1:
                    return 0 if s[0] == control_char else 1
                else:
                    return 0
            current_len = len(s)
        return current_len
