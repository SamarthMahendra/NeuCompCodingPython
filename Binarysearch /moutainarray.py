class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        def find_piviot():
            l = mountainArr.length()
            low, high = 0, l - 1
            while low < high:
                mid = (low + high) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    low = mid + 1
                else:
                    high = mid
            return low

        pivot = find_piviot()

        # Standard binary search in ascending order
        def binary_search_asc(low, high):
            while low <= high:
                mid = (low + high) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        # Search in the ascending part
        index = binary_search_asc(0, pivot)
        if index != -1:
            return index

        # Binary search in descending order
        def binary_search_desc(low, high):
            while low <= high:
                mid = (low + high) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:  # Since it's descending, move left
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        # If not found, search in the descending part
        return binary_search_desc(pivot + 1, n - 1)