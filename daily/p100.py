# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        current_p, current_q = p, q
        stack_p, stack_q = [], []

        if (current_p and not current_q) or (not current_p and current_q):
            return False

        while current_p and current_q:
            if current_p.val != current_q.val:
                return False

            if current_p.right and current_q.right:
                stack_p.append(current_p.right)
                stack_q.append(current_q.right)
            elif (not current_p.right and current_q.right) or (current_p.right and not current_q.right):
                return False

            if current_p.left and current_q.left:
                current_p = current_p.left
                current_q = current_q.left
            elif ((not current_p.left) and current_q.left) or (current_p.left and (not current_q.left)):
                return False
            else:
                if stack_p and stack_q:
                    current_p = stack_p.pop()
                    current_q = stack_q.pop()
                elif (not stack_p and stack_q) or (stack_p and not stack_q):
                    return False
                else:
                    break
        return True
