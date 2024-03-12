# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        current = head
        while current:
            current = current.next
            counter += 1

        steps = counter - n
        if steps == 0:
            return head.next

        counter = 0
        root = head
        while root:
            if counter == steps - 1:
                root.next = root.next.next
                break
            root = root.next
            counter += 1

        return head
