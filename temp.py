def countSubarraysWithSumK(nums, k):
    # Initialize the hashmap to store prefix sums and their frequencies
    prefix_sum_count = {0: 1}  # Base case: one way to have a sum of 0 (empty subarray)
    current_sum = 0
    count = 0

    for num in nums:
        # Update the running sum
        current_sum += num

        # Check if there exists a prefix sum that makes up the difference
        if current_sum - k in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]

        # Update the hashmap with the current prefix sum
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count


# Example usage:
nums = [2, 1, 2, 1]
k = 4
print("Number of subarrays with sum k:", countSubarraysWithSumK(nums, k))
