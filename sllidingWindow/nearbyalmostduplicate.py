class Solution:

    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        from sortedcontainers import SortedList
        sorted_list = SortedList()

        for i, num in enumerate(nums):

            pos = sorted_list.bisect_left(num - valueDiff)

            if pos < len(sorted_list) and abs(sorted_list[pos] - num) <= valueDiff:
                return True

            sorted_list.add(num)

            if i >= indexDiff:
                sorted_list.remove(nums[i - indexDiff])

        return False
