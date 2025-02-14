# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = res = ListNode()
        cur, pur = list1, list2
        while cur and pur:
            if cur.val <= pur.val:
                res.next = cur
                cur = cur.next
            else:
                res.next = pur
                pur = pur.next
            res = res.next
        if cur:
            res.next = cur
        if pur:
            res.next = pur
        return head.next

