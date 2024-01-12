from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        current = root
        each_branch_div = []
        branch_list = []
        stack, break_point = [], []
        branch_counter = 0

        while current:
            branch_list.append(current.val)
            branch_counter += 1
            if current.right:
                stack.append(current.right)
                break_point.append(branch_counter)

            if current.left:
                current = current.left
            else:
                if stack:
                    each_branch_div.append(max(branch_list) - min(branch_list))
                    current = stack.pop()
                    return_point = break_point.pop()
                    branch_list = branch_list[:return_point]
                    branch_counter = len(branch_list)
                else:

                    each_branch_div.append(max(branch_list) - min(branch_list))
                    break

        return max(each_branch_div)


# [2, 4, 3, 1, null, 0, 5, null, 6, null, null, null, 7]
root = TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(0)))
root = TreeNode(
    2, TreeNode(4, TreeNode(1, None, TreeNode(6)), None), TreeNode(3, TreeNode(0), TreeNode(5, None, TreeNode(7)))
)
a = Solution()
print(a.maxAncestorDiff(root))
