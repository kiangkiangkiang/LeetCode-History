# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_leaf(self, root):
        result = []
        stack = []
        current = root
        while current or stack:
            if current.right:
                stack.append(current.right)

            if current.left:
                current = current.left
            else:
                if not current.right:
                    result.append(current.val)
                if stack:
                    current = stack.pop()
                else:
                    break
        print(result)
        return result

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return True if self.get_leaf(root1) == self.get_leaf(root2) else False
