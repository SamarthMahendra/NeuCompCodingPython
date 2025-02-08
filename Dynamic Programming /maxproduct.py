def maxProduct(nums):
    # Edge case: if nums is empty, return 0
    if not nums:
        return 0

    # Initialize the current maximum, current minimum, and result with the first element.
    cur_max = cur_min = result = nums[0]

    # Iterate through the list, starting from the second element.
    for num in nums[1:]:
        # If num is negative, swap the current maximum and minimum.
        if num < 0:
            cur_max, cur_min = cur_min, cur_max

        # Update the current maximum and current minimum products.
        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)

        # Update the global maximum product.
        result = max(result, cur_max)

    return result


# Example usage:
nums1 = [2, 3, -2, 4]
print(maxProduct(nums1))  # Output: 6

nums2 = [-2, 0, -1]
print(maxProduct(nums2))  # Output: 0