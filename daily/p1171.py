# Given the head of a linked list,
# we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

# After doing so, return the head of the final linked list.
# You may return any such answer.


# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Example 1:

# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# Example 2:

# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# Example 3:

# Input: head = [1,2,3,-3,-2]
# Output: [1]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import defaultdict
from typing import Optional


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        prev = None
        hash_check = defaultdict(list)
        hast_state = []
        state_counter = 0
        accumulate = 0
        while head:
            hash_check[head.val].append((prev, head, state_counter))
            hast_state.append(hash_check)
            state_counter += 1
            accumulate += head.val
            if accumulate == 0:
                prev = None
                head = head.next
                root = head
                hash_check = defaultdict(list)
                continue
            else:
                if prev:
                    if accumulate in hash_check and hash_check[accumulate]:
                        remain_prev, remain_head, index = hash_check[accumulate].pop()
                        hash_check = hast_state[index]
                        if remain_head:
                            prev = remain_head
                            remain_head.next = head.next
                            head = head.next
                        else:
                            prev = None
                            head = head.next
                            root = head
                        continue
                    else:
                        pass
            prev = head
            head = head.next

        return root


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        accumulate = 0
        index = 0
        root = head
        history = defaultdict(list)
        history_state = []
        while head:
            accumulate += head.val
            if accumulate == 0:
                head = head.next
                root = head
                history = defaultdict(list)
                history_state.append(history)
            else:
                if accumulate in history and history[accumulate]:
                    history_head, index = history[accumulate].pop()
                    history = history_state[index]
                    head = head.next
                    history_head.next = head
                    root = head
                else:
                    history[head.val].append((head, index))
                    history_state.append(history)
                    head = head.next
            index += 1
        return root
