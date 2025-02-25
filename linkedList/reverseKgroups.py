# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(root):
            prev = None
            while root:
                root.next, prev, root = prev, root, root.next
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            # we need next to connect further
            nxt = tail.next
            # this will go to reverse fn
            rev = prev.next
            tail.next = None

            prev.next = reverse(rev)

            # since rev was first node before, now its last node, connect ahead
            rev.next = nxt

            prev = rev






