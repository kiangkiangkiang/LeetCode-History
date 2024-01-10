from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_next_infect(self, infect_node: int, who_infect_me: int) -> list:
        return [i for i in self.node_to_adjacent[infect_node] if i != who_infect_me]

    def get_adjacent(self, root: TreeNode) -> dict:
        pass

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.node_to_adjacent = self.get_adjacent(root)
        current_infect_list, prev_infect_list = [[start]], [[None]]
        infect_counter = 0
        while current_infect_list:
            new_prev_infect, next_infect_list = [], []
            for current_infect, prev_infect in current_infect_list, prev_infect_list:
                tmp = []
                for c in current_infect:
                    next_infect_list.append(self.get_next_infect(infect_node=c, who_infect_me=prev_infect[0]))
                    tmp.append(c)
                new_prev_infect.append(tmp)

            prev_infect_list = new_prev_infect
            current_infect_list = next_infect_list
            infect_counter += 1
        return infect_counter
