# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head

        def reverse(root):
            if root is None or root.next is None:
                return root
            prev = None
            while root:
                root.next, prev, root = prev, root, root.next
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow.next
        slow.next = None

        reversedhalf = reverse(mid)

        first, second = head, reversedhalf

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


