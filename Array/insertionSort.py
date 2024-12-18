def insertionSort(nums):
    if len(nums) == 1:
        return nums

    for j in range(1, len(nums)):
        key = nums[j]
        i = j-1
        while i >= 0 and key <= nums[i]:

            nums[i+1] =  nums[i]
            i -= 1
        nums[i+1] = key
    return nums


nums = [ 3, 1, 6, 2]
print(insertionSort(nums))