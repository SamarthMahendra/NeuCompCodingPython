class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr_by_distance = sorted(arr, key=lambda num: (abs(num - x), num))
        top_k_closest = arr_by_distance[:k]
        return sorted(top_k_closest)


