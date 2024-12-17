# Leetcode 300
from bisect import bisect_left


def lengthOfLIS(nums, current_index, prev_index):
    if current_index == len(nums):
        return 0

    else:
        exclude = lengthOfLIS(nums, current_index+1, prev_index)

        include = 0
        if prev_index == -1 or nums[current_index] > nums[prev_index]:
            include = 1 + lengthOfLIS(nums, current_index+1, current_index)

    return max(exclude, include)



def lengthOfLIS(nums):
    dp = []
    [dp.append(num) if (pos:=bisect_left(dp, num)) == len(dp) else dp.__setitem__(pos, num) for num in nums]
    return len(dp)

def lengthOfLIS(nums):
    dp = []
    for num in nums:
        if (pos:=bisect_left(dp, num)) == len(dp):
            dp.append(num)
        else:
            dp[pos] = num
    return len(dp)


# test case
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", lengthOfLIS(arr, 0, -1))