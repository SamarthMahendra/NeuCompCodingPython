# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow, fast = head, head

        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse second half
        prev = None
        cur = slow.next
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        slow.next = None

        first, second = head, prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2








