# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque, defaultdict(list)
from typing import Iterable, List, Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack_node, sign_stack = deque(), deque()
        left_check_store: Iterable[bool] = defaultdict(deque)
        index_store: defaultdict(deque)
        index_stack: Iterable[int] = deque()
        current_index = 0
        current = root
        current_sign = None
        while current or stack_node:
            next_pointer, next_sign = None, None
            index_store[current_index].appendleft(current.val)
            left_check_store[current_index].appendleft(current_sign)

            if current.right:
                stack_node.append(current.right)
                sign_stack.append(False)
                index_stack.append(current_index)

            if current.left:
                stack_node.append(current.left)
                sign_stack.append(True)
                index_stack.append(current_index)

            if stack_node:
                next_pointer = stack_node.popleft()
                next_sign = sign_stack.popleft()
                current_index = index_stack.popleft()

            current = next_pointer
            current_sign = next_sign
            current_index += 1
        print(left_check_store)

        bottom = index_store.pop()
        sign = left_check_store.pop()

        if True not in sign.values():
            return bottom[0]
        else:
            for val, s in zip(bottom.values(), sign.values()):
                if s:
                    return val 

