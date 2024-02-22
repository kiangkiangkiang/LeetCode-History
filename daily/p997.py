# In a town, there are n people labeled from 1 to n.
# There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi]
# representing that the person labeled ai trusts the person labeled bi.
# If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates_sum = {i: 0 for i in range(1, n + 1)}
        candidates = list(range(1, n + 1))
        trust.sort()

        prev = None
        for trust_relation in trust:
            candidates_sum[trust_relation[1]] += 1
            if prev != trust_relation[0]:
                candidates.remove(trust_relation[0])

            prev = trust_relation[0]

        if candidates:
            for i in candidates:
                if candidates_sum[i] == n - 1:
                    return i

        return -1


n = 2
trust = [[1, 2]]
n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
# n = 2
# trust = [[1, 2], [2, 1]]
n = 3
trust = [[1, 2], [2, 3]]
n = 4
trust = [[1, 2], [3, 2], [1, 3], [4, 1], [3, 1], [2, 1], [2, 3], [4, 3], [4, 2], [3, 4], [2, 4]]
a = Solution()
print(a.findJudge(n, trust))
