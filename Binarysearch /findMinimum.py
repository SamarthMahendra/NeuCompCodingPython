def findMin(nums):
    low, high = 0, len(nums) - 1

    # Check if the array is not rotated
    if nums[low] <= nums[high]:
        return nums[low]

    # Binary search to find the minimum element
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
