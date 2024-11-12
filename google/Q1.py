def max_digit(arr):
    maxnum = 0
    n = len(arr)
    for i in range(n):
        num1 = arr[i]
        maxnum = max(maxnum, num1)
        if i + 1 < n:
            num2 = num1 * 10 + arr[i + 1]
            maxnum = max(maxnum, num2)
            if i + 2 < n:
                num3 = num2 * 10 + arr[i + 2]
                maxnum = max(maxnum, num3)
    return maxnum


# Test cases
arr = [7, 2, 3, 3, 4, 9]
print(max_digit(arr))  # Output: 749

arr2 = [0, 0, 5, 7]
print(max_digit(arr2))  # Output: 57

