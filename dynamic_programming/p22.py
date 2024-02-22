# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

from collections import deque

# Input: n = 1
# Output: ["()"]
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def merge(s_list):
            result = []
            for s in s_list:
                for i in range(len(s)):
                    result.append(s[:i] + "()" + s[i:])
            return result

        def helper(current_n):
            if current_n == 1:
                return ["()"]
            elif current_n > 1:
                return merge(helper(current_n=current_n - 1))

        return list(set(helper(n)))


a = Solution()
n = 3
print(a.generateParenthesis(n))
