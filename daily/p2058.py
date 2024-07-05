# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [-1, -1]

        critical_index = []
        counter = 1
        last_val = None

        while head:
            if last_val:
                if head.next:
                    # minima
                    if last_val > head.val and head.next.val > head.val:
                        critical_index.append(counter)

                    # maxima
                    elif last_val < head.val and head.next.val < head.val:
                        critical_index.append(counter)

            last_val = head.val
            head = head.next
            counter += 1

        if len(critical_index) < 2:
            return [-1, -1]
        else:
            critical_index.sort()
            minimum = 10000000
            pointer = 0
            while pointer < len(critical_index) - 1:
                current = critical_index[pointer + 1] - critical_index[pointer]
                if current < minimum:
                    minimum = current
                pointer += 1
            return [minimum, critical_index[-1] - critical_index[0]]
