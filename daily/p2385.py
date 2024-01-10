from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    node_to_adjacent = defaultdict(set)

    def get_next_infect(self, infect_node: int, who_infect_me: int) -> list:
        return [i for i in self.node_to_adjacent[infect_node] if i != who_infect_me]

    def get_adjacent(self, root: TreeNode) -> dict:
        current = root
        stack = []
        while current or stack:
            if current.right:
                self.node_to_adjacent[current.val].add(current.right.val)
                self.node_to_adjacent[current.right.val].add(current.val)
                stack.append(current.right)
            if current.left:
                self.node_to_adjacent[current.val].add(current.left.val)
                self.node_to_adjacent[current.left.val].add(current.val)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                else:
                    break

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.get_adjacent(root)
        current_infect_list, prev_infect_list = [[start]], [[None]]
        infect_counter = 0
        while current_infect_list:
            new_prev_infect, next_infect_list = [], []
            for current_infect, prev_infect in zip(current_infect_list, prev_infect_list):
                tmp = []
                breakpoint()
                for c in current_infect:
                    next_infect = self.get_next_infect(infect_node=c, who_infect_me=prev_infect[0])
                    if not next_infect:
                        new_prev_infect.append([])
                    else:
                        tmp.append(c)
                    next_infect_list.append(next_infect)
                new_prev_infect.append(tmp)
                print(next_infect_list)

            prev_infect_list = new_prev_infect
            current_infect_list = next_infect_list
            infect_counter += 1

        return infect_counter


root = TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(6)))
start = 2

a = Solution()
print(a.amountOfTime(root, start))
