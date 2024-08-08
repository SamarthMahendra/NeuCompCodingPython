class Quicksort:


    def __init__(self):
        pass

    @staticmethod
    def qucikSort(nums, low, high):
        if low< high:
            # find pivot that is sorted
            pivot = Quicksort.partition(nums, low, high)

            # quicksort on left and rightside of pivot
            Quicksort.qucikSort(nums, low, pivot-1)
            Quicksort.qucikSort(nums, pivot+1, high)

    @staticmethod
    def partition(nums, low, high):
        pivot = nums[high]
        left = 0
        right = high - 1

        while True:

            while left<= right and nums[left] <= pivot:
                left+=1

            while right>=left and nums[right] >= pivot:
                right-=1

            if left>right:
                break

            nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[high] = nums[high], nums[left]

        return left


arr = [3, 5, 1, 2, 0]
Quicksort.qucikSort(arr, 0, len(arr)-1)
print(arr)







