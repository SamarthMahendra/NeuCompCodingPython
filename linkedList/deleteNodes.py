
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a set of values to delete for efficient lookups
        to_delete = set(nums)

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next:
            if cur.next.val in to_delete:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next