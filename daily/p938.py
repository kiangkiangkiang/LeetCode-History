from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_in_range(self, val, low, high):
        if low <= val <= high:
            return val
        else:
            return False

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        current = root
        stack = []
        my_sum = 0
        test = []
        while current or stack:
            test += [current.val] if current else [None]
            # go other road
            if not current and stack:
                current = stack.pop()

            # Add
            add_val = self.check_in_range(current.val, low, high)
            my_sum += add_val if add_val else 0

            # Check if other road
            if current.right:
                stack.append(current.right)

            # Next
            current = current.left
        print(f"test = {test}")
        return my_sum
