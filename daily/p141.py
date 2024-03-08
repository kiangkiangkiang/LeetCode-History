from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memory = set()
        while head:
            if head not in memory:
                memory.add(head)
            else:
                return True
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one_step = head
        two_step = head
        while one_step and two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next
            if one_step == two_step:
                return True
        return False
