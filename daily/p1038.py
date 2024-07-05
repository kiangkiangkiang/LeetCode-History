# 1038. Binary Search Tree to Greater Sum Tree
# Medium
# Topics
# Companies
# Hint
# Given the root of a Binary Search Tree (BST),
# convert it to a Greater Tree such that every key of the original BST
# is changed to the original key plus the sum of all keys greater
# than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


def show(root):
    current = root
    stack = []
    while current:
        print(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            current = current.right
        else:
            if stack:
                current = stack.pop()
            else:
                break


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        new_root = root
        stack = []
        my_list = deque()
        total = 0
        while root:
            if root.left:
                tmp = root
                stack.append(tmp)

            if root.right:
                root.val += total
                root = root.right
            else:
                total += root.val
                if stack:
                    root = stack.pop()
                    root.val += total
                    total = root.val
                    root = root.left
                else:
                    break
        show(new_root)
        return new_root


root = TreeNode(
    val=4,
    left=TreeNode(val=1, left=TreeNode(0), right=TreeNode(2, None, TreeNode(3))),
    right=TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))),
)
# root = [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]
# [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

a = Solution()
print(a.bstToGst(root))
