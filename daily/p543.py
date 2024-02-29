# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def get_max_branch_length(self, root: Optional[TreeNode]) -> int:
        this_pointer = root
        stack = []
        counter_stack = []
        counter = 0
        max_length = 0
        while this_pointer or stack:
            counter += 1
            next_pointer = None

            if this_pointer.right:
                stack.append(this_pointer.right)
                counter_stack.append(counter)

            if this_pointer.left:
                next_pointer = this_pointer.left
            else:
                if not stack:
                    break
                next_pointer = stack.pop()
                counter = counter_stack.pop()
            if counter > max_length:
                max_length = counter

            this_pointer = next_pointer

        return max_length + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_total, right_total = 0, 0
        if root.left:
            left_total = self.get_max_branch_length(root.left)
            print(left_total)
        if root.right:
            right_total = self.get_max_branch_length(root.right)
            print(right_total)
        return left_total + right_total
