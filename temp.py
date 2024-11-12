import random
import string


# TODO: Define a merge_sort function that takes data to sort and returns the sorted data
def merge_sort(arr):
    # TODO: If the alphanumeric array has one or no elements, it is already sorted. So, return the array immediately.
    if len(arr) <= 1:
        return arr

    # TODO: Next, divide the array into two equal parts.
    mid = len(arr) // 2
    # TODO: Sort the left and right parts of the array with the merge_sort function.
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # TODO: After sorting both halves of the array, combine them together using the merge function.
    return merge(left, right)


# TODO: In the merge function, take two sorted arrays as inputs
def merge(left, right):
    result = list()
    l, r = 0, 0
    while l < len(left) and r < len(right):
        # TODO: While both arrays have elements in them, compare the first element of each.
        if left[l] >= right[r]:
            result.append(left[l])
            l += 1
        # If the first element of the left array is smaller, add it to the result array and remove it from the left array.
        # Otherwise, do the same with the right array.
        else:
            result.append(right[r])
            r += 1

    # TODO: If the left or right array still has elements, add them to the result array.
    result.extend(left[l:])
    result.extend(right[r:])
    return result


# TODO: Generate some random data to sort
numbers = [random.randint(0, 10) for i in range(20)]
# TODO: Print the original data
print(numbers)

# TODO: Use your merge_sort function to sort the data
sorted_numbers = merge_sort(numbers)

# TODO: Print the sorted data
print(sorted_numbers)