# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

from collections import deque

a = deque("123")
print(a.__len__)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_deque = deque(s)
        t_deque = deque(t)
        while s_deque and t_deque:
            if s_deque[0] == t_deque[0]:
                s_deque.popleft()
                t_deque.popleft()
            else:
                t_deque.popleft()
        return False if s_deque else True


s = "abc"
t = "ahbgdc"
a = Solution()
print(a.isSubsequence(s, t))
