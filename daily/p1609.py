# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0,
# its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level,
# all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level,
#  all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree,
# return true if the binary tree is Even-Odd, otherwise return false.

# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
from typing import Optional


class Solution:
    def __init__(self):
        self.level_value_tbl = defaultdict(list)

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        current_level = 1
        current_pointer = root
        stack_node, stack_level = [], []
        while current_pointer or stack_node:
            next_pointer = None

            # Check Even-Odd Tree
            if current_level % 2 == 0:
                if current_pointer.val % 2 != 0:
                    return False

                if current_level in self.level_value_tbl:
                    if self.level_value_tbl[current_level][-1] <= current_pointer.val:
                        return False
            else:
                if current_pointer.val % 2 == 0:
                    return False
                if current_level in self.level_value_tbl:
                    if self.level_value_tbl[current_level][-1] >= current_pointer.val:
                        return False

            self.level_value_tbl[current_level].append(current_pointer.val)

            # DFS
            if current_pointer.right:
                stack_node.append(current_pointer.right)
                stack_level.append(current_level)

            if current_pointer.left:
                next_pointer = current_pointer.left
            else:
                if stack_node:
                    next_pointer = stack_node.pop()
                    current_level = stack_level.pop()

            current_pointer = next_pointer
            current_level += 1

        return True


r = TreeNode(2, TreeNode(10), TreeNode(4))
a = Solution()
print(a.isEvenOddTree(r))
