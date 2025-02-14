# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while slow and fast.next and slow.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True

        return False
