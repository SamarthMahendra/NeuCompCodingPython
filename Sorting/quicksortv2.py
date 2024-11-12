


def quicksort(nums):
    if len(nums) <= 1:
        return  nums
    else:
        pivot = nums[0]
        lesser = [n for n in nums if n < pivot]
        middle = [n for n in nums if n  == pivot]
        greater = [n for n in nums if n > pivot]
        return quicksort(lesser) + middle + quicksort(greater)


# test 
arr = [3, 5, 1, 2, 0]
print(quicksort(arr))  # Output: [0, 1, 2, 3, 5]
