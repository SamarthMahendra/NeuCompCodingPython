numsv1 =  [1,2,3,4,5,5]
numsv2 =  [1,2,3,4,5]
def checkDuplicates(nums):
    lookup = {}


    for number in nums:
        if number in lookup:
            return True
        else:
            lookup[number] = 1
    return False




def containsDuplicate(nums: List[int]) -> bool:
    return not(len(nums) == len(set(nums)))


print(checkDuplicates(numsv1))
print(checkDuplicates(numsv2))

