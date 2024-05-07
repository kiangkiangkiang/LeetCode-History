# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def get_reverse(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            if tmp:
                head = tmp
            else:
                break
        return head

    def double_it(self, head):
        last_acc = 0
        root = head
        while head:
            tmp = head.val * 2
            if tmp >= 10:
                current_acc = 1
                tmp -= 10
            else:
                current_acc = 0

            current_add = tmp + last_acc
            if current_add >= 10:
                current_add -= 10
                current_acc += 1

            head.val = current_add
            last_acc = current_acc
            if head.next:
                head = head.next
            else:
                if last_acc:
                    head.next = ListNode(last_acc)
                break

        return root

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_r = self.get_reverse(head)
        print(head_r)
        head_r = self.double_it(head_r)
        print(head_r)
        return self.get_reverse(head_r)
