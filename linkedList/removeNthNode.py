# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        i, j = 0, 0
        while cur:
            cur = cur.next
            i += 1

        pos = i - n

        if pos == 0:
            return head.next

        cur = head
        for _ in range(pos-1):
            cur = cur.next

        cur.next = cur.next.next

        return head
