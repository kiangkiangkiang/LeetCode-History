# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return root

        current = root
        stack = []
        current_depth = 1
        while current:
            if stack:
                next_current = stack.pop()
            else:
                depth += 1

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

            current = next_current
