# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pt1, pt2 = headA, headB

        while pt1 != pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA

        return pt1


# test case
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = ListNode(1)
# headB.next.next.next = headA.next.next

# A - > 4 -> 1 -> 8 -> 4 -> 5
# B - > 5 -> 0 -> 1 -> 8 -> 4 -> 5


obj = Solution()
print(obj.getIntersectionNode(headA, headB).val) # Output: 8